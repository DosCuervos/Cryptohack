#!/usr/bin/env python3

def xor_decrypt(ciphertext, key):
    decrypted = ""
    key_repeated = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]
    for i in range(len(ciphertext)):
        decrypted += chr(ord(ciphertext[i]) ^ ord(key_repeated[i]))
    return decrypted

ciphertext = input()
key = "OpenAIisAmazing"

decrypted_text = xor_decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)

