import csv
from models.event import Event
from utils.file_manager import FileManager

class EventRepository:
    def __init__(self, test_mode=False):
        self.file = "test_data/events.csv" if test_mode else "data/events.csv"
        self.file_manager = FileManager()

    def get_all(self):
        rows = self.file_manager.read_csv(self.file)
        return [
            Event(
                int(r['id']),
                r['title'],
                r['description'],
                r['date_time'],
                r['location'],
                int(r['capacity'])
            )
            for r in rows
        ]

    def get_by_id(self, event_id):
        events = self.get_all()
        for e in events:
            if e.id == event_id:
                return e
        return None

    def add(self, title, description, date_time, location, capacity):
        events = self.file_manager.read_csv(self.file)

        new_id = 1
        if events:
            new_id = max(int(e['id']) for e in events) + 1

        events.append({
            'id': new_id,
            'title': title,
            'description': description,
            'date_time': date_time,
            'location': location,
            'capacity': capacity
        })

        self.file_manager.write_csv(
            self.file,
            ['id', 'title', 'description', 'date_time', 'location', 'capacity'],
            events
        )

    def delete(self, event_id):
        events = self.file_manager.read_csv(self.file)
        events = [e for e in events if int(e['id']) != event_id]

        self.file_manager.write_csv(
            self.file,
            ['id', 'title', 'description', 'date_time', 'location', 'capacity'],
            events
        )
