class User:
    def __init__(self, id, username, role):
        self.id = int(id)
        self.username = username
        self.role = role  # student / admin
