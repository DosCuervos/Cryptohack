#!/usr/bin/env python3

FLAG = b'crypto{biscuits}'


def decode_binary_string(plaintext):
    return ''.join(chr(int(plaintext[i*8:i*8+8],2)) for i in range(len(plaintext)//8))


a = b'crypto{biscuits}'
plaintext = ''.join([bin(i)[2:].zfill(8) for i in a])
print(plaintext)

print(decode_binary_string(plaintext))
