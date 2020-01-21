#!/usr/bin/python3
class MyList(list):
    def __init__(self):
        pass

    def print_sorted(self):
        newlist = self.copy()
        print(sorted(newlist))
