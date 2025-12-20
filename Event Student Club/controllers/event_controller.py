from flask import Blueprint, render_template, request, redirect, session
from repositories.event_repository import EventRepository
from repositories.registration_repository import RegistrationRepository

event_bp = Blueprint('event', __name__)

event_repo = EventRepository()
reg_repo = RegistrationRepository()


@event_bp.route('/events')
def list_events():
    """
    Display all events with optional search
    """
    query = request.args.get('q', '')
    events = event_repo.get_all()

    if query:
        events = [e for e in events if query.lower() in e.title.lower()]

    return render_template('list_events.html', events=events)


@event_bp.route('/events/<int:event_id>')
def event_detail(event_id):
    """
    Display event details and registration status
    """
    event = event_repo.get_by_id(event_id)
    if not event:
        return "Event not found"

    registrations = reg_repo.get_by_event(event_id)
    registered_count = len(registrations)

    return render_template(
        'event_detail.html',
        event=event,
        registered_count=registered_count,
        registrations=registrations
    )


@event_bp.route('/events/<int:event_id>/register', methods=['POST'])
def register_event(event_id):
    """
    Register logged-in student to an event
    """
    # User must be logged in
    if 'user_id' not in session:
        return redirect('/login')

    student_id = session['user_id']
    event = event_repo.get_by_id(event_id)

    if not event:
        return "Event not found"

    # Check if already registered
    if reg_repo.exists(student_id, event_id):
        return "You are already registered for this event"

    # Capacity check
    current_count = reg_repo.count_by_event(event_id)
    if event.capacity and current_count >= event.capacity:
        return "Event capacity is full"

    # Register student
    reg_repo.add(student_id, event_id)
    return redirect(f'/events/{event_id}')
@event_bp.route('/events/<int:event_id>/unregister', methods=['POST'])
def unregister_event(event_id):
    if 'user_id' not in session:
        return redirect('/login')

    student_id = session['user_id']

    if not reg_repo.exists(student_id, event_id):
        return redirect(f'/events/{event_id}')

    reg_repo.remove(student_id, event_id)
    return redirect(f'/events/{event_id}')
