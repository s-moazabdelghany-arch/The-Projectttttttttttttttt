class Event:
    def __init__(self, id, title, description, date_time, location, capacity):
        self.id = int(id)
        self.title = title
        self.description = description
        self.date_time = date_time
        self.location = location
        try:
            self.capacity = int(capacity) if capacity != '' else None
        except:
            self.capacity = None

    def __repr__(self):
        return f"Event({self.id},{self.title})"
