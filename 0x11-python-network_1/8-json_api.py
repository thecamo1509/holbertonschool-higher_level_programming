#!/usr/bin/python3
import requests
from sys import argv, exit

q = ""
if len(argv) > 1:
    q = argv[1]
r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
try:
    if len(r.json()) == 0:
        print("No result")
        exit()
    myid = "[{}]".format(str(r.json()['id']))
    print(myid + " " + r.json()['name'])
except ValueError:
    print("Not a valid JSON")
