from flask import Blueprint, jsonify, request

from src.data.check_in_handler import CheckInHandler
from src.http_types.http_request import HttpRequest

check_in_route_bp = Blueprint("check_in_routes", __name__)


@check_in_route_bp.route("/attendees/<attendee_id>/check-in", methods=["POST"])
def create_check_in(attendee_id):
    http_request = HttpRequest(param={"attendee_id": attendee_id})
    checkin_handler = CheckInHandler()
    http_response = checkin_handler.register(http_request)
    return jsonify(http_response.body), http_response.status_code
