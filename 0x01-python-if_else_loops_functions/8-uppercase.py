#!/usr/bin/env python3
def uppercase(str):
	for letter in str:
		num = ord(letter)
		if num > 96 and num < 123:
			num = num - 32
		print("{:c}".format(num), end='')
	print("")