#!/usr/bin/env python3

binary = input()
total = 0

i = 0
while i < len(binary):
    digit = int(binary[i])
    power = len(binary) - i - 1

    total += digit * (2 ** power)

    i = i + 1

print(total)
