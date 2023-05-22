from .api.stats import Stats
from flask_socketio import SocketIO
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
monitor = Stats()
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("connect")
def stats():
    print("connected")
    while True:
        socketio.emit("updateStats", monitor.get())
        socketio.sleep(3)
