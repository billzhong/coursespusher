#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests
from bs4 import BeautifulSoup
import json
import os
from boxcar import push


def c1700():
    COURSEURL = 'http://www.cs.mun.ca/courses/cs1700/'
    COURSENAME = '1700'
    COURSEUSERNAME = 'cs1700'
    COURSEPASSWORD = 'fall13'
    try:
        r = requests.get(COURSEURL, auth=(COURSEUSERNAME, COURSEPASSWORD))
    except requests.exceptions.ConnectionError:
        exit(1)
    soup = BeautifulSoup(r.text)

    data = []
    for div in soup.find_all('div', id='news'):
        for li in div.find_all('li'):
            data.append(li.get_text())
    newData = data

    if os.path.isfile(COURSENAME + '.json'):
        f = open(COURSENAME + '.json', 'r')
        oldData = json.loads(f.read())
        f.close()
    else:
        oldData = []

    diffData = []

    if not oldData:
        diffData = newData
    elif newData[0] != oldData[0]:
        for i in xrange(len(newData) - len(oldData)):
            diffData.append(newData[i])

    diffData.reverse()

    f = open(COURSENAME + '.json', 'w')
    f.write(json.dumps(data))
    f.close()
    push(COURSENAME, COURSEURL, diffData)
