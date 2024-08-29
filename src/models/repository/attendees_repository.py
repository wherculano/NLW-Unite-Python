from typing import Dict, List

from sqlalchemy.exc import IntegrityError, NoResultFound

from src.models.entities.attendees import Attendees
from src.models.entities.check_ins import CheckIns
from src.models.entities.events import Events
from src.models.settings.connection import db_connection_handler


class AttendeesRepository:
    def insert_attendee(self, attendee_info: Dict) -> Dict:
        with db_connection_handler as db:
            try:
                attendee = Attendees(
                    id=attendee_info.get("uuid"),
                    name=attendee_info.get("name"),
                    email=attendee_info.get("email"),
                    event_id=attendee_info.get("event_id"),
                )
                db.session.add(attendee)
                db.session.commit()
                return attendee_info
            except IntegrityError:
                raise Exception("Attendee already exists!")
            except Exception as exception:
                db.session.rollback()
                raise exception

    def get_attendee_badge_by_id(self, attendee_id: str) -> Attendees:
        with db_connection_handler as db:
            try:
                attendee = (
                    db.session
                    .query(Attendees)
                    .join(Events, Events.id == Attendees.event_id)
                    .filter(Attendees.id == attendee_id)
                    .with_entities(Attendees.name, Attendees.email, Events.title)
                    .one()
                )
                return attendee
            except NoResultFound:
                return

    def get_attendees_by_event_id(self, event_id: str) -> List[Attendees]:
        with db_connection_handler as db:
            attendees = (
                db.session.
                query(Attendees)
                .outerjoin(CheckIns, CheckIns.attendeeId == Attendees.id)
                .filter(Attendees.event_id == event_id)
                .with_entities(
                    Attendees.id,
                    Attendees.name,
                    Attendees.email,
                    Attendees.created_at.label("attendee_created_at"),
                    CheckIns.created_at.label("checked_at"),
                )
                .all()
            )
            return attendees
