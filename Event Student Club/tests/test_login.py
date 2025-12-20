from repositories.user_repository import UserRepository

def test_user_login():
    repo = UserRepository(test_mode=True)
    user = repo.get_by_username("admin")
    assert user is not None
