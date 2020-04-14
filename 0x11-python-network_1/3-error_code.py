#!/usr/bin/python3

import urllib.request
from sys import argv

url = argv[1]
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html)
except urllib.error.HTTPError as e:
    print('Error code: {}'.format(e.code))
