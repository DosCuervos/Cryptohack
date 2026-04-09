#!/usr/bin/env python3

from pwn import *

cypher = bytes.fromhex("53656e64696e673a202f686f6d652f64617665792f446f63756d656e74732f57656c636f6d652041626f6172642e706466")
key = (b'OpenAIisAmazing')

#key = ''.join(chr(c ^ m) for c, m in zip(cypher, plaintext))

#print(key)

flag = xor(cypher, key)

print(flag)

#another solution from someone else
#from pwn import xor
#flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
#print(xor(flag, 'crypto{'.encode())) # oh, it says 'myXORke+y...'
#print(xor(flag, 'myXORkey'.encode())) # try this? yay, it works! sometimes simpler is better
