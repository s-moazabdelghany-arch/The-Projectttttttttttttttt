from models.registration import Registration
from utils.file_manager import FileManager

class RegistrationRepository:
    def __init__(self):
        self.fm = FileManager()

    def get_all(self):
        rows = self.fm.read_csv('registrations.csv')
        return [Registration(r['id'], r['student_id'], r['event_id'], r.get('reg_date','')) for r in rows]

    def get_by_student(self, student_id):
        rows = self.fm.read_csv('registrations.csv')
        return [Registration(r['id'], r['student_id'], r['event_id'], r.get('reg_date','')) for r in rows if int(r['student_id'])==int(student_id)]

    def get_by_event(self, event_id):
        rows = self.fm.read_csv('registrations.csv')
        return [Registration(r['id'], r['student_id'], r['event_id'], r.get('reg_date','')) for r in rows if int(r['event_id'])==int(event_id)]

    def exists(self, student_id, event_id):
        rows = self.fm.read_csv('registrations.csv')
        for r in rows:
            if int(r['student_id'])==int(student_id) and int(r['event_id'])==int(event_id):
                return True
        return False

    def add(self, student_id, event_id):
        rows = self.fm.read_csv('registrations.csv')
        next_id = 1
        if rows:
            next_id = max(int(r['id']) for r in rows)+1
        rows.append({'id':str(next_id),'student_id':str(student_id),'event_id':str(event_id),'reg_date':''})
        self.fm.write_csv('registrations.csv', ['id','student_id','event_id','reg_date'], rows)
