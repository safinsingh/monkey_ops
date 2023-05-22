from monkey import app, monitor

if __name__ == "__main__":
    monitor.monitor()
    app.run(debug=True, port=8080)
