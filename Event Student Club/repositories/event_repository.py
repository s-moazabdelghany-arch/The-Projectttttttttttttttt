from models.event import Event
from utils.file_manager import FileManager

class EventRepository:
    def __init__(self):
        self.fm = FileManager()

    def get_all(self):
        rows = self.fm.read_csv('events.csv')
        return [Event(r['id'], r['title'], r['description'], r['date_time'], r['location'], r.get('capacity','')) for r in rows]

    def get_by_id(self, id):
        rows = self.fm.read_csv('events.csv')
        for r in rows:
            if int(r['id']) == int(id):
                return Event(r['id'], r['title'], r['description'], r['date_time'], r['location'], r.get('capacity',''))
        return None
