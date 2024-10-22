#!/usr/bin/env python3

decimal = int(input())
hexa = ""
code = "0123456789abcdef"

while decimal != 0:
    hexa += code[decimal % 16]
    decimal //= 16

hexa = hexa[::-1]

i = 0
while i < len(hexa) and not ("a" <= hexa[i] <= "f"):
    i = i + 1

if i < len(hexa):
    print(hexa[i])
