from monkey import app, stats, db

if __name__ == "__main__":
    stats.monitor()
    app.run(debug=True, port=8080)
