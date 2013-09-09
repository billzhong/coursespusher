#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests


def push(name, url, data):

    SECRET = 'nE0hFEktDNbSsKhMxdbC0AziXwIm1PQteBSYg4RI'
    KEY = 'dXGsO0NnJZsxdZc6R2zN'
    for i in data:
        payload = {
            'secret': SECRET,
            'notification[from_screen_name]': name,
            'notification[message]': i,
            'notification[source_url]': url
        }
        requests.post('http://boxcar.io/devices/providers/' + KEY + '/notifications/broadcast', data=payload)
