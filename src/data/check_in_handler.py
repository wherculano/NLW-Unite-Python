import json

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.repository.check_ins_repository import CheckInsRepository


class CheckInHandler:
    def __init__(self) -> None:
        self.__check_in_repository = CheckInsRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        attendee_id = http_request.param["attendee_id"]
        response = self.__check_in_repository.insert_check_in(attendee_id)
        if "detail" in response:
            return HttpResponse(body=response, status_code=409)
        return HttpResponse(body=response, status_code=201)
