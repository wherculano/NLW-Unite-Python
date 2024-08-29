from uuid import uuid4

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.events_repository import EventRepository


class AttendeesHandler:
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()
        self.__events_repository = EventRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        event_id = http_request.param["event_id"]

        event_count_attendees = self.__events_repository.count_event_attendees(event_id)
        if (
            event_count_attendees["attendeesAmount"]
            and event_count_attendees["maximumAttendees"]
            < event_count_attendees["attendeesAmount"]
        ):
            raise Exception("The event is crowded!")

        body["uuid"] = str(uuid4())
        body["event_id"] = event_id
        self.__attendees_repository.insert_attendee(attendee_info=body)
        return HttpResponse(body=None, status_code=201)

    def get_attendee_badge(self, http_request: HttpRequest) -> HttpResponse:
        attendee_id = http_request.param["attendee_id"]
        badge = self.__attendees_repository.get_attendee_badge_by_id(attendee_id)
        if not badge:
            raise Exception("Attendee not found!")
        return HttpResponse(
            body={
                "badge": {
                    "name": badge.name,
                    "email": badge.email,
                    "eventTitle": badge.title,
                }
            },
            status_code=200,
        )
