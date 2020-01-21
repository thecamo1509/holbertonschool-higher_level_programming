#!/usr/local/bin/python3
import json
import sys
save_to_json = __import__('7-save_to_json_file').save_to_json_file
load_from_json = __import__('8-load_from_json_file').load_from_json_file


try:
    mylist = load_from_json("add_item.json")

except FileNotFoundError:
    mylist = []
finally:
    save_to_json(mylist, "add_item.json")
    i = 1
    for i in range(1, len(sys.argv)):
        mylist.append(sys.argv[i])
