#!/usr/bin/python3
import requests
from sys import argv, exit

if len(argv) < 3:
    exit()
api = "https://api.github.com"
url = api + "/repos/" + argv[2] + "/" + argv[1] + "/commits"
r = requests.get(url).json()
count = 0
for i in r:
    print(i['sha'] + ": " + i['commit']['author']['name'])
    count += 1
    if count == 10:
        break
