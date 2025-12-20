class Student:
    def __init__(self, id, name, email):
        self.id = int(id)
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Student({self.id},{self.name})"
