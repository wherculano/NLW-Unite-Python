import pytest
from uuid import uuid4

from src.models.repository.events_repository import EventRepository
from src.models.settings.connection import db_connection_handler


db_connection_handler.connect_to_db()

ID_TEST = str(uuid4())


@pytest.mark.skip(reason="Dont want to create a new event.")
def test_inser_event():
    event = {
        "uuid": ID_TEST,
        "title": "Event test",
        "details": "Test inserting data.",
        "slug": f"event-test-{ID_TEST[:8]}",
        "maximum_attendees": 10
    }
    event_repository = EventRepository()
    response = event_repository.insert_event(event)
    print(f"Successfully created: {response}")


@pytest.mark.skip(reason="There is no event with a new ID.")
def test_get_event_by_id():
    db_connection_handler.connect_to_db()
    event_id = ID_TEST
    event_repository = EventRepository()
    response = event_repository.get_event_by_id(event_id)
    print(response)
