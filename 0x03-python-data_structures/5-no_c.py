#!/usr/bin/env python3
def no_c(my_string):
    newstring = ""
    for i in range(0, len(my_string)):
        if my_string[i] == "c" or my_string[i] == "C":
            newstring = newstring + ""
        else:
            newstring = newstring + my_string[i]
    return(newstring)
