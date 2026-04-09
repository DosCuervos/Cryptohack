#!/usr.bin/env python3

from random import randint

a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{biscuits}'

#plaintext = text to binary
#for binary octet? in plaintext perfom powers func
#e = random integer between 1 and p(modulus)
#n = for new int("b") pow(a , random exponent, p(modulus)
# if "b" is coprime append ciphertext list
# if "b" is n
def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext

print(encrypt_flag(FLAG))
