#!/usr/bin/env python3

check = int(input("Input a number to check: "))

def odd_even(check):
	if check % 2 == 0:
		print(str(check) + " is Even!!!")
	else:
		print(str(check) + " is Odd!!!")

odd_even(check)
