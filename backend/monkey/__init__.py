from .api.stats import Stats
from flask_socketio import SocketIO
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
stats = Stats()
socketio = SocketIO(app, cors_allowed_origins="*")
