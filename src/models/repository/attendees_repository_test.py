import pytest
from uuid import uuid4

from src.models.repository.attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler


db_connection_handler.connect_to_db()

ATTENDEE_ID_TEST = str(uuid4())
EVENT_ID = "27c54d87-cd11-48c8-b6be-0fda2496fac4"  # Use your local event id


@pytest.mark.skip(reason="Dont want to create a new attendee.")
def test_insert_attendee():
    attendee = {
        "uuid": ATTENDEE_ID_TEST,
        "name": "John Doe",
        "email": "john@doe.com",
        "event_id": EVENT_ID,
    }
    attendee_repository = AttendeesRepository()
    response = attendee_repository.insert_attendee(attendee)
    print(f"Successfully created: {response}")


@pytest.mark.skip(reason="There is no event with a new ID.")
def test_get_attendee_badge_by_id():
    attendee_id = ATTENDEE_ID_TEST
    attendee_repository = AttendeesRepository()
    response = attendee_repository.get_attendee_badge_by_id(attendee_id)
    print(response)
