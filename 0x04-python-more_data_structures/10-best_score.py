#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = 0
    biggestkey = ""
    if(a_dictionary):
        for i in a_dictionary:
            if a_dictionary[i] >= biggest:
                biggest = a_dictionary[i]
                biggestkey = i
        return(biggestkey)
    else:
        return(None)