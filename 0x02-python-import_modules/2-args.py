#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    qty = len(sys.argv)
    if qty == 1:
        print("{:d} arguments.".format(qty - 1))
    else:
        if qty == 2:
            print("{:d} argument:".format(qty - 1))
        else:
            print("{:d} arguments:".format(qty - 1))
        for i in range(1, qty):
            print("{:d}: {:s}".format(i, sys.argv[i]))
