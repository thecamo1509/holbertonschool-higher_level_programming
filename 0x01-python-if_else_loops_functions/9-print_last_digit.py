#!/usr/bin/python3
def print_last_digit(number):
    last = 0
    if number < 0:
        number = number * (-1)
        last = number % 10
    last = number % 10
    print(last, end='')
    return last
