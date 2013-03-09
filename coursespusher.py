#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests
from bs4 import BeautifulSoup
import re
import json
import os
from apscheduler.scheduler import Scheduler
import logging


SECRET = 'nE0hFEktDNbSsKhMxdbC0AziXwIm1PQteBSYg4RI'
KEY = 'dXGsO0NnJZsxdZc6R2zN'


def c3719():

    COURSEURL = 'http://www.cs.mun.ca/~kol/courses/3719-w13/'
    COURSENAME = '3719'
    r = requests.get(COURSEURL)
    soup = BeautifulSoup(r.text)

    data = []
    for i in soup.ul.contents:
        temp = re.sub('<[^>]*>', '', str(i))
        data.append(str(temp).lstrip(' ').rstrip(' \n'))
    data = data[1:]

    if not os.path.isfile(COURSENAME + '.json'):
        f = open(COURSENAME + '.json', 'w')
        f.write(json.dumps(data))
        f.close()

    newData = json.loads(json.dumps(data))

    f = open(COURSENAME + '.json', 'r')
    oldData = json.loads(f.read())
    f.close()

    if newData[0] != oldData[0]:
        updated = True
    else:
        updated = False

    if updated:
        f = open(COURSENAME + '.json', 'w')
        f.write(json.dumps(data))
        f.close()

        payload = {
            'secret': SECRET,
            'notification[from_screen_name]': COURSENAME,
            'notification[message]': newData[0],
            'notification[source_url]': COURSEURL
        }
        requests.post('http://boxcar.io/devices/providers/' + KEY + '/notifications/broadcast', data=payload)

if __name__ == '__main__':
    logging.basicConfig(filename='debug.log', level=logging.DEBUG)
    sched = Scheduler()
    sched.daemonic = False
    sched.add_interval_job(c3719, hours=1)
    sched.start()

    while True:
        i = raw_input('Enter "exit" to stop: ')
        if i == 'exit':
            sched.shutdown()
            break