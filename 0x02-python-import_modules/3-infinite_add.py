#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    qty = len(sys.argv)
    ans = 0
    if qty == 1:
        print(0)
    else:
        for i in range(1, qty):
            ans = ans + int(sys.argv[i])
    print("{}".format(ans))
