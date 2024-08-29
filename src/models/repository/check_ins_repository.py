import json
from typing import Dict

from sqlalchemy.exc import IntegrityError

from src.errors.error_types.http_409_conflict import HttpConflictError
from src.models.entities.check_ins import CheckIns
from src.models.settings.connection import db_connection_handler


class CheckInsRepository:
    def insert_check_in(self, attendee_id: str) -> Dict:
        with db_connection_handler as db:
            try:
                checkin = CheckIns(attendee_id=attendee_id)
                db.session.add(checkin)
                db.session.commit()
                return {
                    "created_at": checkin.created_at,
                    "attendee_id": checkin.attendee_id,
                }
            except IntegrityError:
                raise HttpConflictError("Check-in already exists.")
            except Exception as exception:
                db.session.rollback()
                raise exception
