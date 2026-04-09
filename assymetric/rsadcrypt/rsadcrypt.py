#!usr/bin/env python3

from Crypto.Util.number import inverse

p = 857504083339712752489993810777

q = 1029224947942998075080348647219

e = 65537

c = 77578995801157823671636298847186723593814843845525223303932

N = (p * q)

phi = (p - 1) * (q - 1)

d = inverse(e, phi)

M = pow(c, d, N)

print(M)
