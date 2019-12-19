#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    convertedToList = list(set(my_list))
    for i in range(len(convertedToList)):
        sum += convertedToList[i]
    return(sum)
