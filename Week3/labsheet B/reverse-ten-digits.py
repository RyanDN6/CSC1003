#!/usr/bin/env python3

total = 0

i = 0
while i < 10:
    n = int(input())
    total += n * (10 ** (9 - i))
    i += 1

i = 0
while i < 10:
    digit = total % 10
    print(digit)

    total //= 10
    i += 1
