from repositories.registration_repository import RegistrationRepository

def test_unregister_event():
    repo = RegistrationRepository(test_mode=True)

    repo.add(student_id=1, event_id=1)
    repo.remove(student_id=1, event_id=1)

    assert not repo.exists(1, 1)
