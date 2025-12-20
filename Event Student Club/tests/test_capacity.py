from repositories.event_repository import EventRepository

def test_event_capacity():
    repo = EventRepository(test_mode=True)

    event = repo.get_all()[0]

    assert event.capacity >= 0
