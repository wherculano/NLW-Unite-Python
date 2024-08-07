from typing import Dict
from src.models.entities.attendees import Attendees
from src.models.entities.events import Events
from src.models.settings.connection import db_connection_handler

from sqlalchemy.exc import IntegrityError, NoResultFound


class AttendeesRepository:
    def insert_attendee(self, attendee_info: Dict) -> Dict:
        with db_connection_handler as db:
            try:
                attendee = Attendees(
                    id = attendee_info.get("uuid"),
                    name = attendee_info.get("name"),
                    email = attendee_info.get("email"),
                    event_id = attendee_info.get("event_id"),
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
                    .with_entities(
                        Attendees.name,
                        Attendees.email,
                        Events.title
                    )
                    .one()
                )
                return attendee
            except NoResultFound:
                return
