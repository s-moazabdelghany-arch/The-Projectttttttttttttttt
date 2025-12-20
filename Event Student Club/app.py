from app_factory import create_app

from controllers.event_controller import event_bp
from controllers.student_controller import student_bp
from controllers.auth_controller import auth_bp
from controllers.admin_controller import admin_bp

app = create_app()

app.register_blueprint(event_bp)
app.register_blueprint(student_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

@app.route('/')
def home():
    return '<a href="/login">Login</a>'


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",  
        port=5000,
        debug=True
    )

app = create_app()
