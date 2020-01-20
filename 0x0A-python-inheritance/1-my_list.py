#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        newlist = self.copy()
        print(sorted(newlist))
