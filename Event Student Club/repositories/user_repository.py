import csv
from models.user import User
from utils.file_manager import FileManager

class UserRepository:
    def __init__(self, test_mode=False):
        self.file = "test_data/users.csv" if test_mode else "data/users.csv"
        self.file_manager = FileManager()

    def get_all(self):
        rows = self.file_manager.read_csv(self.file)
        return [User(int(r['id']), r['username'], r['role']) for r in rows]

    def get_by_username(self, username):
        users = self.get_all()
        for user in users:
            if user.username == username:
                return user
        return None
