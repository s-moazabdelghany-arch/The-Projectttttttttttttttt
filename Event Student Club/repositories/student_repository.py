from models.student import Student
from utils.file_manager import FileManager

class StudentRepository:
    def __init__(self):
        self.fm = FileManager()

    def get_all(self):
        rows = self.fm.read_csv('students.csv')
        return [Student(r['id'], r['name'], r['email']) for r in rows]

    def get_by_id(self, id):
        rows = self.fm.read_csv('students.csv')
        for r in rows:
            if int(r['id']) == int(id):
                return Student(r['id'], r['name'], r['email'])
        return None
