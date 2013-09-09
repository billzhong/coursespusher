#!/usr/bin/env python
# -*- coding: utf8 -*-

from apscheduler.scheduler import Scheduler
import logging
from comp3719 import c3719


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