#!/usr/bin/python3
def magic_string(word=[-1]):
    word[0] += 1
    print(word[0])
    return "Holberton, " * word[0] + "Holberton"
