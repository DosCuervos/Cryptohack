#!/usr/bin/env python3

from pwn import *

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

lock = xor(state, round_key)    
flag = [list(lock[i:i+4]) for i in range(0,  len(lock), 4)]

def matrix2bytes(flag):
    return bytes(sum(flag, []))

print(matrix2bytes(flag))
