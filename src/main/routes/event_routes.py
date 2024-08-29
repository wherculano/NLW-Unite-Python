from flask import Blueprint, jsonify, request

from src.data.event_handler import EventHandler
from src.errors.error_handler import http_handler
from src.http_types.http_request import HttpRequest

event_route_bp = Blueprint("event_routes", __name__)


@event_route_bp.route("/events", methods=["POST"])
def creat_event():
    try:
        http_request = HttpRequest(body=request.json)
        event_handler = EventHandler()
        http_response = event_handler.register(http_request=http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = http_handler(exception)
        return jsonify(http_response.body), http_response.status_code


@event_route_bp.route("/events/<event_id>", methods=["GET"])
def get_event(event_id):
    try:
        http_request = HttpRequest(param={"event_id": event_id})
        event_handler = EventHandler()
        http_response = event_handler.find_by_id(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = http_handler(exception)
        return jsonify(http_response.body), http_response.status_code
