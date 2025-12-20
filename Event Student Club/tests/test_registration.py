from repositories.registration_repository import RegistrationRepository

def test_register_event():
    repo = RegistrationRepository()
    repo.add(1, 1)
    assert repo.exists(1, 1) == True
