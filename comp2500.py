#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests
from bs4 import BeautifulSoup
import json
import os
from boxcar import push


def c2500():

    COURSEURL = 'http://www.cs.mun.ca/~brown/2500/'
    COURSENAME = '2500'
    COURSEUSERNAME = 'student'
    COURSEPASSWORD = 'bluebell'
    try:
        r = requests.get(COURSEURL, auth=(COURSEUSERNAME, COURSEPASSWORD))
    except requests.exceptions.ConnectionError:
        exit(1)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text)

    data = []
    for p in soup.find_all('p', align='LEFT'):
        data.append(p.get_text().replace(u'\u2013', '-').replace('\n', ' '))
    newData = data[::-1]

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
