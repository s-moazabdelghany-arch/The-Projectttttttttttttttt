from repositories.registration_repository import RegistrationRepository

def test_register_event():
    repo = RegistrationRepository(test_mode=True)

    repo.add(student_id=1, event_id=1)

    assert repo.exists(1, 1)
