from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Monkey ops</p>"
