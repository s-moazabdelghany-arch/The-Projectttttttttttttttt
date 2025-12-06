from flask import Blueprint, render_template
from repositories.student_repository import StudentRepository
from repositories.registration_repository import RegistrationRepository
from repositories.event_repository import EventRepository

student_bp = Blueprint('student', __name__, url_prefix='/students')

student_repo = StudentRepository()
reg_repo = RegistrationRepository()
event_repo = EventRepository()

@student_bp.route('/')
def list_students():
    students = student_repo.get_all()
    return render_template('students_list.html', students=students)

@student_bp.route('/<int:student_id>')
def profile(student_id):
    s = student_repo.get_by_id(student_id)
    regs = reg_repo.get_by_student(student_id)
    events = [event_repo.get_by_id(r.event_id) for r in regs]
    return render_template('profile.html', student=s, events=events)
