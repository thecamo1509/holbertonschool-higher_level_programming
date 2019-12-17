#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    list_len = len(my_list)
    if idx < 0:
        return(None)
    if idx > list_len:
        return(None)
    while i <= idx:
        i = i + 1
    return(i)
