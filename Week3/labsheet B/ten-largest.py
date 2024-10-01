#!/usr/bin/env python3

maximum = int(input())

i = 0
while i < 9:
    n = int(input())

    if n > maximum:
        maximum = n

    i += 1

print(maximum)
