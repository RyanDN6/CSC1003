#!/usr/bin/env python3

n = int(input()) + 1

total = 1

i = 1
while i < n:
    total *= i
    i += 1

print(total)
