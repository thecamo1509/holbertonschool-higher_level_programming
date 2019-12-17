#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        biggest = 0
        if len(my_list) == 0:
            return(None)
        for i in range(len(my_list)):
            if int(my_list[i]) >= biggest:
                biggest = int(my_list[i])
        return(biggest)
