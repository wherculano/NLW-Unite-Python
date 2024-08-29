import json
from typing import Dict
from src.models.entities.check_ins import CheckIns
from src.models.settings.connection import db_connection_handler

from sqlalchemy.exc import IntegrityError


class CheckInsRepository:
    def insert_check_in(self, attendee_id: str) -> Dict:
        with db_connection_handler as db:
            try:
                checkin = CheckIns(attendee_id=attendee_id)
                db.session.add(checkin)
                db.session.commit()
                checkin = {
                    "created_at": checkin.created_at,
                    "attendee_id": checkin.attendee_id,
                }
                return checkin
            except IntegrityError:
                return {"detail": "Check-in already exists."}
            except Exception as exception:
                db.session.rollback()
                raise exception
