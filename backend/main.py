from monkey_api import app, stats


if __name__ == "__main__":
    stats.monitor()
    app.run(debug=True, port=8080)
