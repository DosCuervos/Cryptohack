#!/usr/bin/env python3

a = int(input())
b = int(input())

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		(gcd, u, v) = egcd(b % a, a)
		return (gcd, v - (b // a) * u, u)

gcd, u, v = egcd(a, b)
print("GCD: {}".format(gcd))
print("u, v: {},{}".format(u, v))
print(" FLAG: crypto{{{},{}}}".format(u, v))
