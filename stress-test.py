#!bin/python3

import argparse
from stress_test.request_thread import RequestThread

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--calls', type=int, help='Amount of calls to be done per each Thread')
parser.add_argument('-t', '--threads', type=int, help='Amount of Threads to be used')
parser.add_argument('--host', type=str, help='IP address or hostname to be called')

arguments = parser.parse_args()

calls = arguments.calls or 10
threads = arguments.threads or 1
host = arguments.host or 'http://localhost/'

if not host.startswith('http'):
    print('[WARN] - Protocol not selected, using default (HTTP)')
    host = 'http://' + host

threads_pool = []

for i in range(threads):
    name = 'thread-{id}'.format(id=i)
    thread = RequestThread(name=name, calls_amount=calls, address=host)
    threads_pool.append(thread)
    thread.start()
