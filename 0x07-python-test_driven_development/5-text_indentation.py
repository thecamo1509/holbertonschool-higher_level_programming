#!/usr/bin/python3
def text_indentation(text):
    flag = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        for c in(text):
            if c == '.' or c == '?' or c == ':':
                flag = 1
                print(c, end='')
                continue
            if flag == 1 and c == ' ':
                c = ''
                print('\n')
                flag = 0
            else:
                print(c, end='')
                flag = 0
