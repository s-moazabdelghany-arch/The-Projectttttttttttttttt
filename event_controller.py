from flask import Blueprint, render_template, request, redirect
from repositories.event_repository import EventRepository
from repositories.registration_repository import RegistrationRepository

event_bp = Blueprint('event', __name__)

event_repo = EventRepository()
reg_repo = RegistrationRepository()

@event_bp.route('/events')
def list_events():
    q = request.args.get('q','')
    events = event_repo.get_all()
    if q:
        events = [e for e in events if q.lower() in e.title.lower()]
    return render_template('list_events.html', events=events)

@event_bp.route('/events/<int:event_id>')
def event_detail(event_id):
    e = event_repo.get_by_id(event_id)
    regs = reg_repo.get_by_event(event_id)
    return render_template('event_detail.html', event=e, registrations=regs)

@event_bp.route('/events/<int:event_id>/register', methods=['POST'])
def register(event_id):
    student_id = request.form.get('student_id')
    if not student_id:
        return redirect(f'/events/{event_id}')
    if reg_repo.exists(student_id, event_id):
        return redirect(f'/events/{event_id}')
    reg_repo.add(student_id, event_id)
    return redirect(f'/events/{event_id}')
