#!/usr/bin/python3

import urllib.parse
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html)
