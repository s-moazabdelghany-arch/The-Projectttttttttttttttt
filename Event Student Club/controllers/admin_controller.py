from flask import Blueprint, render_template, request, redirect, session
from repositories.event_repository import EventRepository
from flask import send_file
import os

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
event_repo = EventRepository()

def admin_only():
    return session.get('role') == 'admin'

@admin_bp.route('/events')
def admin_events():
    if not admin_only():
        return "Access Denied"
    return render_template('admin_events.html', events=event_repo.get_all())

@admin_bp.route('/events/add', methods=['GET','POST'])
def add_event():
    if not admin_only():
        return "Access Denied"
    if request.method == 'POST':
        event_repo.add(
            request.form['title'],
            request.form['description'],
            request.form['date_time'],
            request.form['location'],
            request.form['capacity']
        )
        return redirect('/admin/events')
    return render_template('add_event.html')

@admin_bp.route('/events/delete/<int:event_id>')
def delete_event(event_id):
    if not admin_only():
        return "Access Denied"
    event_repo.delete(event_id)
    return redirect('/admin/events')

@admin_bp.route('/export/registrations')
def export_registrations():
    if not admin_only():
        return "Access Denied"
    path = os.path.join('data', 'registrations.csv')
    return send_file(path, as_attachment=True)
