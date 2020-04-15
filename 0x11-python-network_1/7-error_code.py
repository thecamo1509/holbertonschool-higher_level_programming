#!/usr/bin/python3
import requests
from sys import argv, exit

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
        exit()
    print(r.text)
