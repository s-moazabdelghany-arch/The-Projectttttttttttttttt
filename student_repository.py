import csv
from models.student import Student
from utils.file_manager import FileManager

class StudentRepository:
    def __init__(self, test_mode=False):
        self.file = "test_data/users.csv" if test_mode else "data/users.csv"
        self.file_manager = FileManager()

    def get_all(self):
        rows = self.file_manager.read_csv(self.file)
        return [
            Student(int(r['id']), r['username'], r['role'])
            for r in rows if r['role'] == 'student'
        ]

    def get_by_id(self, student_id):
        students = self.get_all()
        for s in students:
            if s.id == student_id:
                return s
        return None
