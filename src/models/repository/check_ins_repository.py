from src.models.entities.check_ins import CheckIns
from src.models.settings.connection import db_connection_handler

from sqlalchemy.exc import IntegrityError


class CheckInsRepository:
    def insert_check_in(self, attendee_id: str) -> str:
        with db_connection_handler as db:
            try:
                checkin = CheckIns(attendeeId=attendee_id)
                db.session.add(checkin)
                db.session.commit()
                return checkin
            except IntegrityError:
                raise Exception("Check In já cadastrado")
            except Exception as exception:
                db.session.rollback()
                raise exception
