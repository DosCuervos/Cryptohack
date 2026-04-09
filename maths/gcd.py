#!/usr/bin/env python3

print("Please put input a & b")
a = int(input())
b = int(input())


def gcd(a,b):
	if a<b:
		a,b = b,a
	while b!=0:
		t = b
		b = a % b
		a = t
	print(a)

gcd(a,b)


