#!/usr/bin/env python3

from pwn import xor
import codecs

cipher = b'hello'
print(cipher)

ciphertext = bytes.hex(cipher)

print(ciphertext)
print(hex(7))

key = hex(int(b'7'))

encrypt = xor(ciphertext, key)

print(encrypt)



secret = b'\x06@\x01\x05NT\x06\x1b\x01V'

decrypt = xor(secret, key)

print(decrypt)

original = codecs.decode(decrypt, 'hex')

print(original)