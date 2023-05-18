from ..monitor import running_container_stats
from time import sleep
import threading

class Stats:
    def __init__(self):
        self.mux = threading.Lock()
        self.stats = {}

    def monitor(self):
        self.thread = threading.Thread(target=self.run_monitor)
        self.thread.start()

    def run_monitor(self):
        while True:
            try:
                with self.mux:
                    self.stats = {"status": "ok", "data": running_container_stats()}
            except:
                with self.mux:
                    self.stats = {"status": "error"}
            sleep(3)

    def get(self):
        with self.mux:
            return self.stats
