#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests


def push(name, url, data):

    SECRET = ''
    KEY = ''
    for i in data:
        payload = {
            'secret': SECRET,
            'notification[from_screen_name]': name,
            'notification[message]': i,
            'notification[source_url]': url
        }
        requests.post('http://boxcar.io/devices/providers/' + KEY + '/notifications/broadcast', data=payload)
