#!/usr/bin/env python3

digits = [0] * 10

n = input()
while n != "end":
    n = int(n)

    digits[n] += 1

    n = input()

i = 0
while i < 10:
    print(i, "*" * digits[i])
    i = i + 1
