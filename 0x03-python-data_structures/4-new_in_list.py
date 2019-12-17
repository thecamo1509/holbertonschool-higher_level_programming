#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = my_list.copy()
    i = 0
    list_len = len(my_list)
    if my_list:
        if idx < 0 or idx >= list_len:
            return(newlist)
        newlist[idx] = element
        return(newlist)
