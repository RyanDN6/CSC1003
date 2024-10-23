#!/usr/bin/env python3

hexa = input()
binary = ""
digits = "0123456789abcdef"
decimal = 0

i = 0
while i < len(hexa):
    j = 0
    while j < len(digits) and digits[j] != hexa[i]:
        j = j + 1

    decimal += j * (16 ** (len(hexa) - i - 1))
    i = i + 1

while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal //= 2

if binary:
    print(binary)
else:
    print(0)
