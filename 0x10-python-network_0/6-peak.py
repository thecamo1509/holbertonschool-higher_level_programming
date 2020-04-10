#!/usr/bin/python3
def find_peak(list_of_integers):
    """This function will get the peak"""
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        peak = list_of_integers[-1]
    else:
        peak = None
    return (peak)
