#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r') as f:
        accumulated = ""
        while True:
            lines = f.readline()
            if lines == '':
                break
            accumulated += lines
            if search_string in accumulated:
                accumulated = accumulated + new_string

    with open(filename, 'w') as fw:
        fw.write(accumulated)
