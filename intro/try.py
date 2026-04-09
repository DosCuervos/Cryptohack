#!/usr/bin/env python3

from pwn import *

cypher = bytes.fromhex("2c11065a1f2c271f28100050242c1401043d140e4a043d0a04133315100b0b280a18")
plaintext = (b'picoCTF{')

key = ''.join(chr(c ^ m) for c, m in zip(cypher, plaintext))

print(key)

flag = xor(cypher, key)

print(flag)

#another solution from someone else
#from pwn import xor
#flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
#print(xor(flag, 'crypto{'.encode())) # oh, it says 'myXORke+y...'
#print(xor(flag, 'myXORkey'.encode())) # try this? yay, it works! sometimes simpler is better
