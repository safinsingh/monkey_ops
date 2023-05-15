from flask import Flask
from monitor import running_container_stats

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Monkey ops</p>"


@app.route("/stats")
def stats():
    return running_container_stats()
