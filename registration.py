class Registration:
    def __init__(self, id, student_id, event_id, reg_date):
        self.id = int(id)
        self.student_id = int(student_id)
        self.event_id = int(event_id)
        self.reg_date = reg_date

    def __repr__(self):
        return f"Registration({self.id}, s:{self.student_id}, e:{self.event_id})"
