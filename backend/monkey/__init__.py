from .api.stats import Stats
from flask_socketio import SocketIO
from flask import Flask, request
from flask_login import LoginManager, UserMixin, login_user
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from sqlalchemy.exc import IntegrityError
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

login_manager = LoginManager()
login_manager.init_app(app)
monitor = Stats()
socketio = SocketIO(app, cors_allowed_origins="*")
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))

    __table_args__ = (UniqueConstraint("username"),)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def check_pw(self, pw: str):
        if bcrypt.checkpw(pw.encode("utf-8"), self.password):
            return True
        else:
            return False

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError:
            db.session.remove()
            return None


def init_users():
    new_user = User("Test", "Test")
    new_user.create()
    print(new_user)


@app.route("/signup", methods=["POST"])
def signup():
    username = request.get_json().get("username")
    password = request.get_json().get("password")

    try:
        new_user = User(username, password)
        new_user.create()
        return f"Used ID {new_user.id} created"
    except IntegrityError:
        return "Username is taken"


@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.get_json().get("username")
    password = request.get_json().get("password")

    user = db.session.query(User).filter_by(username=username).first()

    if user.check_pw(password):
        login_user(user)
        return f"User ID {user.id} logged in"
    return "Could not log in"


@app.before_first_request
def before_first_request():
    db.create_all()


@socketio.on("connect")
def stats():
    print("connected")
    while True:
        socketio.emit("updateStats", monitor.get(), namespace="")
        socketio.sleep(3)
