#!/usr/bin/python3
def find_peak(list_of_integers):
    if len(list_of_integers) != 0:
        peak = list_of_integers[0]
        for i in range(len(list_of_integers)):
            if list_of_integers[i] != peak:
                if list_of_integers[i] > list_of_integers[i - 1] \
                   and list_of_integers[i] > list_of_integers[i + 1]:
                    peak2 = list_of_integers[i]
                    if peak2 > peak:
                        peak = peak2
        return(peak)
