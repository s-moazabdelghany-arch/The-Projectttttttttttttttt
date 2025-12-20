from flask import Blueprint, render_template, session, redirect
from repositories.student_repository import StudentRepository
from repositories.registration_repository import RegistrationRepository
from repositories.event_repository import EventRepository

# Blueprint
student_bp = Blueprint('student_bp', __name__)

# Repositories
student_repo = StudentRepository()
registration_repo = RegistrationRepository()
event_repo = EventRepository()


# ===============================
# ADMIN: View All Students
# ===============================
@student_bp.route('/students', strict_slashes=False)
def list_students():
    # Only admin can view all students
    if session.get('role') != 'admin':
        return redirect('/events')

    students = student_repo.get_all()
    return render_template('students_list.html', students=students)


# ===============================
# STUDENT / ADMIN: View Profile
# ===============================
@student_bp.route('/students/<int:student_id>', strict_slashes=False)
def student_profile(student_id):

    # Student can view only his profile
    if session.get('role') != 'admin' and session.get('user_id') != student_id:
        return redirect('/events')

    student = student_repo.get_by_id(student_id)

    registrations = registration_repo.get_by_student(student_id)

    events = []
    for reg in registrations:
        event = event_repo.get_by_id(reg.event_id)
        if event:
            events.append(event)

    return render_template(
        'profile.html',
        student=student,
        events=events
    )
