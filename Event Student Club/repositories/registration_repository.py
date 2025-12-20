import csv
from utils.file_manager import FileManager

class RegistrationRepository:
    def __init__(self, test_mode=False):
        self.file = "test_data/registrations.csv" if test_mode else "data/registrations.csv"
        self.file_manager = FileManager()

    def get_all(self):
        return self.file_manager.read_csv(self.file)

    def get_by_student(self, student_id):
        rows = self.get_all()
        return [r for r in rows if int(r['student_id']) == student_id]

    def exists(self, student_id, event_id):
        rows = self.get_all()
        return any(
            int(r['student_id']) == student_id and int(r['event_id']) == event_id
            for r in rows
        )

    def add(self, student_id, event_id):
        if self.exists(student_id, event_id):
            return

        rows = self.get_all()
        rows.append({
            'student_id': student_id,
            'event_id': event_id
        })

        self.file_manager.write_csv(
            self.file,
            ['student_id', 'event_id'],
            rows
        )

    def remove(self, student_id, event_id):
        rows = self.get_all()
        rows = [
            r for r in rows
            if not (int(r['student_id']) == student_id and int(r['event_id']) == event_id)
        ]

        self.file_manager.write_csv(
            self.file,
            ['student_id', 'event_id'],
            rows
        )
