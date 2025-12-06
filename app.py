from flask import Flask
from controllers.event_controller import event_bp
from controllers.student_controller import student_bp

app = Flask(__name__)
app.register_blueprint(event_bp)
app.register_blueprint(student_bp)

@app.route('/')
def home():
    return ('<h1>Student Club Events</h1>'
            "<p><a href='/events'>View Events</a></p>"
            "<p><a href='/students'>View Students</a></p>")

if __name__ == '__main__':
    app.run(debug=True)
