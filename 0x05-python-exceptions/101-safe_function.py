#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return(result)
    except ZeroDivisionError as zero:
        print("Exception: {}".format(zero), file=stderr)
    except IndexError as index:
        print("Exception: {}".format(index), file=stderr)
