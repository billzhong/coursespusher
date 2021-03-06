#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests
from bs4 import BeautifulSoup
import re
import json
import os
from boxcar import push


def comp3719():

    COURSEURL = 'http://www.cs.mun.ca/~kol/courses/3719-w13/'
    COURSENAME = 'COMP3719'
    try:
        r = requests.get(COURSEURL)
    except requests.exceptions.ConnectionError:
        exit(1)
    soup = BeautifulSoup(r.text)

    data = []
    for i in soup.ul.contents:
        temp = re.sub('<[^>]*>', '', str(i))
        data.append(str(temp).lstrip(' ').rstrip(' \n'))
    data = data[1:]
    newData = map(unicode, data)

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
