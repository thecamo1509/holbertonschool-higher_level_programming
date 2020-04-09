#!/usr/bin/python3
def find_peak(list_of_integers):
    """This function will get the peak"""
    if len(list_of_integers) > 0:
        peak = list_of_integers[0]
        for i in list_of_integers:
            if i > peak:
                peak = i
    else:
        peak = None
    return (peak)
