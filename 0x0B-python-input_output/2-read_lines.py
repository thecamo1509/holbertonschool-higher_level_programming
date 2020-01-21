#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="utf-8") as f:
        if nb_lines > len(f.readlines()):
            f.seek(0)
            print(f.read())
        if nb_lines <= 0:
            f.seek(0)
            print(f.read())
        else:
            f.seek(0)
            for i in range(nb_lines):
                print(f.readline(), end="")
