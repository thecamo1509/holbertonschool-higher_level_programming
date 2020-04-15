#!/usr/bin/python3
import requests
from sys import argv

url = argv[1]
email = argv[2]

r = requests.post(url, data={'email': '{}'.format(email)})
print(r.text)
