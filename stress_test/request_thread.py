import requests
import threading
import time


def current_milli_time():
    return int(round(time.time() * 1000))


class RequestThread(threading.Thread):

    def __init__(self, name: str, calls_amount: int, address: str):
        threading.Thread.__init__(self)
        self.name = name
        self.calls_amount = calls_amount
        self.address = address

    def run(self):
        print('Starting Thread #', self.name)

        start_time = current_milli_time()

        for r in range(self.calls_amount):
            requests.get(self.address)

        end_time = current_milli_time()

        print('Ending Thread #', self.name, end_time - start_time)
