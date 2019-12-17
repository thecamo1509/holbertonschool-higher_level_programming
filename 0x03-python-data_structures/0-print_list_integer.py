#!/usr/bin/python3
def print_list_integer(my_list=[]):
    i = 0
    list_len = len(my_list)
    while i < list_len:
        print("{}".format(my_list[i]))
        i = i + 1
