#!/usr/bin/env python3

minimum = int(input())

i = 0
while i < 9:
    n = int(input())

    if n < minimum and n % 2 == 0:
        minimum = n

    i += 1

print(minimum)
