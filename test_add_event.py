from repositories.event_repository import EventRepository

def test_add_event():
    repo = EventRepository(test_mode=True)

    repo.add(
        title="Test Event",
        description="Test Description",
        date_time="2025-01-01",
        location="Test Hall",
        capacity=10
    )

    events = repo.get_all()
    assert len(events) > 0
