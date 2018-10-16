#!bin/python3

import requests
import time


def current_milli_time():
    return int(round(time.time() * 1000))


start_time = current_milli_time()

for i in range(500):
    r = requests.get('http://192.168.99.100')

    # print(r)

end_time = current_milli_time()

print(end_time - start_time)
