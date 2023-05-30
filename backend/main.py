from monkey import app, socketio

if __name__ == "__main__":
    socketio.run(app, debug=True, port=8080, allow_unsafe_werkzeug=True)
