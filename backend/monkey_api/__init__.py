from .stats import Stats
from flask import Flask
from flask_socketio import SocketIO

stats = Stats()
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
