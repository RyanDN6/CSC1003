#!/usr/bin/env python3

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

alphabet = lower + upper
encrypted = lower[n:] + lower[:n] + upper[n:] + upper[:n]

caesar = {}

i = 0
while i < len(alphabet):
    caesar[encrypted[i]] = alphabet[i]
    i = i + 1

text = sys.stdin.read().strip()

encrypt = ""
i = 0
while i < len(text):
    if text[i] in caesar:
        encrypt += caesar[text[i]]
    else:
        encrypt += text[i]
    i = i + 1

print(encrypt)
