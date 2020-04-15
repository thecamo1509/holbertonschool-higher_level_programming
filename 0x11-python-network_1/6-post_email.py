#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    r = requests.post(url, data={'email': '{}'.format(email)})
    print(r.text)
