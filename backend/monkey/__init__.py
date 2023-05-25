from flask_socketio import SocketIO
from flask import Flask, make_response, request, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from sqlalchemy.exc import IntegrityError
from sqlalchemy import UniqueConstraint
from .monitor import running_container_stats
from time import sleep
import threading

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
socketio = SocketIO(app, cors_allowed_origins="*")
db = SQLAlchemy(app)


def thread_wrapper():
    while True:
        stats = {}
        try:
            stats = {"status": "ok", "data": running_container_stats()}
        except:
            stats = {"status": "error"}
        socketio.emit("updateStats", stats)
        sleep(1)


th = threading.Thread(target=thread_wrapper)
th.start()


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = (UniqueConstraint("username"),)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def check_pw(self, pw: str):
        if bcrypt.checkpw(pw.encode("utf-8"), self.password):
            return True
        else:
            return False


def create_cookie():
    resp = make_response("user session")
    resp.set_cookie("user id", str(session["user_id"]))
    return resp


@app.route("/signup", methods=["POST"])
def signup():
    username = request.get_json().get("username")
    password = request.get_json().get("password")

    try:
        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.id
        return create_cookie()
    except IntegrityError as e:
        db.session.remove()
        return "error creating user " + e


@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.get_json().get("username")
    password = request.get_json().get("password")

    user = db.session.query(User).filter_by(username=username).first()

    if user == None:
        return "user does not exist"
    elif user.check_pw(password):
        session["user_id"] = user.id
        return create_cookie()
    return "password is incorrect"


@app.route("/test", methods=["GET"])
def test():
    return str(session["user_id"])


@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    resp = make_response("logged out")
    resp.delete_cookie("user id")
    return resp


@app.before_first_request
def before_first_request():
    db.create_all()


# @socket.on
