#!/usr/bin/env python3

p = int(input())

def quad(p):
	while True:
		for A in range(1, p):
			print((A**2) % p)
		break	
		 
quad(p)

#Note: input modulo p to find quadratic residue, if x is a quadratic residue
#there will always be two solutions , can use head -(half of p) to see single
#set of quad res integers
