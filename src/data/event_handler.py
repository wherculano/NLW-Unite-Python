from uuid import uuid4
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.repository.events_repository import EventRepository


class EventHandler:
    def __init__(self) -> None:
        self.__events_repository = EventRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body["uuid"] = str(uuid4())
        self.__events_repository.insert_event(event_info=body)
        return HttpResponse(
            body={"eventId": body["uuid"]},
            status_code=201
        )

    def find_by_id(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        event = self.__events_repository.get_event_by_id(event_id)
        if not event:
            return HttpResponse(
                body={"message": "Event not found"},
                status_code=404
            )

        event_count_attendees = self.__events_repository.count_event_attendees(
            event_id)
        return HttpResponse(
            body={
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "details": event.details,
                    "slug": event.slug,
                    "maximumAttendees": event.maximum_attendees,
                    "attendeesAmount": event_count_attendees["attendeesAmount"]
                }
            },
            status_code=200
        )
