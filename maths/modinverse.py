#!/usr/bin/env python3

# multiplicative inverse
# g * d = 1 mod p or represented differently A X? = 1 (mod m)
# the value of 'd'/'x' should be in range of int modulo 'm'
# ex (1,2,...m-1) note: will be under 'm' ex. x = 1-16 if m = 17
### new note pow() function does this more efficiently pow(a ,m-2, m)

a = int(input("A = "))
m = int(input("M = "))

def modinverse(a, m):
	for x in range(1, m):
		if (((a % m) * (x % m)) % m == 1):
			return x
			
flag = modinverse(a, m)
print("Multiplicative inverse is : ", flag)
