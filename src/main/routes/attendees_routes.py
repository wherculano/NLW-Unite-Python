from flask import Blueprint, jsonify, request

from src.data.attendees_handler import AttendeesHandler
from src.http_types.http_request import HttpRequest

attendees_route_bp = Blueprint("attendees_routes", __name__)


@attendees_route_bp.route("/events/<event_id>/register", methods=["POST"])
def create_attendees(event_id: str):
    http_request = HttpRequest(param={"event_id": event_id}, body=request.json)
    attendees_handler = AttendeesHandler()
    http_response = attendees_handler.register(http_request)
    return jsonify(http_response.body), http_response.status_code


@attendees_route_bp.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendee_badge(attendee_id: str):
    http_request = HttpRequest(param={"attendee_id": attendee_id})
    attendees_handler = AttendeesHandler()
    http_response = attendees_handler.get_attendee_badge(http_request)
    return jsonify(http_response.body), http_response.status_code
