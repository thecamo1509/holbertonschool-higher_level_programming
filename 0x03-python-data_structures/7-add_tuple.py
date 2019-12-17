#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tupla1 = (0, 0)
    elif len(tuple_a) == 1:
        tupla1 = (tuple_a[0], 0)
    else:
        tupla1 = tuple_a[0], tuple_a[1]
    if len(tuple_b) == 0:
        tupla2 = (0, 0)
    elif len(tuple_b) == 1:
        tupla2 = (tuple_b[0], 0)
    else:
        tupla2 = tuple_b[0], tuple_b[0]
    newtuple = (tupla1[0] + tupla2[0], tupla1[1] + tupla2[1])
    return(newtuple)
