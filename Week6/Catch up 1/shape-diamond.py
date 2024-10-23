#!/usr/bin/env python3

n = int(input())

i = 0
while i < n // 2:
    print(" " * ((n // 2) - i) + "*" * (1 + (i * 2)))
    i += 1

print("*" * n)

i = 0
while i < n // 2:
    print(" " * (i + 1) + "*" * (n - (2 * i) - 2))
    i += 1
