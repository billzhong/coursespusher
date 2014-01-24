#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests
from bs4 import BeautifulSoup
import json
import os
from boxcar import push


def comp3715():

    COURSEURL = 'http://www.cs.mun.ca/~rod/'
    COURSENAME = 'COMP3715'
    try:
        r = requests.get(COURSEURL)
    except requests.exceptions.ConnectionError:
        exit(1)
    soup = BeautifulSoup(r.text)

    data = []
    for a in soup.find_all('a'):
        if 'cs3715/web' in a['href']:
            data.append(a.get_text())
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