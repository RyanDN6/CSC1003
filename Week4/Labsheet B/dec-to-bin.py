#!/usr/bin/env python3

decimal = int(input())
binary = ""

while decimal != 0:
    binary += str(decimal % 2)
    decimal //= 2

print(binary[::-1])
