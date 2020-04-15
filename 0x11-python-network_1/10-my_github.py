#!/usr/bin/python3
import requests
from sys import argv, exit

if len(argv) < 3:
    exit()
q = (argv[1], argv[2])
r = requests.get('https://api.github.com/user', auth=q).json()
if 'id' in r:
    try:
        print(str(r['id']))
    except ValueError:
        print("Not a valid JSON")
else:
    print("None")
