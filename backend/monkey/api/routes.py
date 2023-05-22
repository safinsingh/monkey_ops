from .. import app, socketio


@app.route("/")
def home():
    return "<p>Monkey ops</p>"
