from . import app, socketio


@app.route("/")
def home():
    return "<p>Monkey ops</p>"


@socketio.on("connect", namespace="/stats")
def stats():
    while True:
        socketio.emit("updateStats", stats.get())
