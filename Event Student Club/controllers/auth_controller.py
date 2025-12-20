from flask import Blueprint, render_template, request, redirect, session
from repositories.user_repository import UserRepository

auth_bp = Blueprint('auth', __name__)

user_repo = UserRepository()


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')

        user = user_repo.get_by_username(username)

        if user:
            session['user_id'] = user.id
            session['role'] = user.role
            session['username'] = user.username

            # Redirect based on role
            if user.role == 'admin':
                return redirect('/admin/events')
            else:
                return redirect('/events')

        return render_template(
            'login.html',
            error="Invalid username"
        )

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
