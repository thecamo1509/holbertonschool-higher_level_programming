#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    newlist = list(map(lambda x: x * number, my_list))
    return(newlist)
