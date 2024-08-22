from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events
from src.models.entities.attendees import Attendees

from sqlalchemy.exc import IntegrityError, NoResultFound


class EventRepository:
    def insert_event(self, event_info: Dict) -> Dict:
        with db_connection_handler as db:
            try:
                event = Events(
                    id=event_info.get("uuid"),
                    title=event_info.get("title"),
                    details=event_info.get("details"),
                    slug=event_info.get("slug"),
                    maximum_attendees=event_info.get("maximum_attendees")
                )
                db.session.add(event)
                db.session.commit()
                return event_info
            except IntegrityError:
                raise Exception("Event already exists!")
            except Exception as exception:
                db.session.rollback()
                raise exception

    def get_event_by_id(self, event_id: str) -> Events:
        with db_connection_handler as db:
            try:
                event = (
                    db.session
                    .query(Events)
                    .filter(Events.id == event_id)
                    .one()
                )
                return event
            except NoResultFound:
                return

    def count_event_attendees(self, event_id: str) -> Dict:
        with db_connection_handler as db:
            event_count = (
                db.session.query(Events)
                .join(Attendees, Events.id == Attendees.event_id)
                .filter(Events.id == event_id)
                .with_entities(Events.maximum_attendees, Attendees.id)
                .all()
            )
            if not len(event_count):
                return {"maximumAttendees": 0, "attendeesAmount": 0}

            return {
                "maximumAttendees": event_count[0].maximum_attendees,
                "attendeesAmount": len(event_count),
            }
