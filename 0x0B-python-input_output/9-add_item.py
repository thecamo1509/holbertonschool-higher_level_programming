#!/usr/bin/python3
import json
import sys
save_to_json = __import__('7-save_to_json_file').save_to_json_file
load_from_json = __import__('8-load_from_json_file').load_from_json_file


try:
    mylist = load_from_json("add_item.json")
except FileNotFoundError:
    mylist = []
finally:
    for i in range(1, len(sys.argv)):
        mylist.append(sys.argv[i])
    save_to_json(mylist, "add_item.json")
