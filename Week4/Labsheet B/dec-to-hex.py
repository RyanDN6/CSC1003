#!/usr/bin/env python3

decimal = int(input())
hex = ""
code = "0123456789abcdef"

while decimal != 0:
    hex += code[decimal % 16]
    decimal //= 16

print(hex[::-1])
