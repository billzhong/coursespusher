#!/usr/bin/env python
# -*- coding: utf8 -*-

from apscheduler.scheduler import Scheduler
import logging
# from comp3719 import comp3719
# from comp2500 import comp2500
# from comp1700 import comp1700
from comp3715 import comp3715


if __name__ == '__main__':
    logging.basicConfig(filename='debug.log', level=logging.DEBUG)
    sched = Scheduler()
    sched.daemonic = False
    # sched.add_interval_job(comp3719, hours=1)
    # sched.add_interval_job(comp2500, hours=2)
    # sched.add_interval_job(comp1700, hours=2)
    sched.add_interval_job(comp3715, hours=2)
    sched.start()

    while True:
        i = raw_input('Enter "exit" to stop: ')
        if i == 'exit':
            sched.shutdown()
            break