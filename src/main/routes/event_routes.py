from flask import Blueprint, jsonify, request

from src.data.event_handler import EventHandler
from src.http_types.http_request import HttpRequest


event_route_bp = Blueprint("event_routes", __name__)


@event_route_bp.route("/events", methods=["POST"])
def creat_event():
    http_request = HttpRequest(body=request.json)
    event_handler = EventHandler()
    http_response = event_handler.register(http_request=http_request)
    return jsonify(http_response.body), http_response.status_code
