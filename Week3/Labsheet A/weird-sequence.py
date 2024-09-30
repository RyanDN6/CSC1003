#!/usr/bin/env python3

n = int(input())
x = 0

i = 0
print(i)

while i < n - 1:

    x = -x + (2 * (x % 2) - 1)

    print(x)

    i += 1
