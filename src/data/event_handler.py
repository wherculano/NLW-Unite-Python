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
