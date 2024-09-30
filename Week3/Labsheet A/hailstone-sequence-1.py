#!/usr/bin/env python3

n = int(input())
hailstone = int(input())

print(hailstone)

i = 0
while i < n - 1:

    if hailstone % 2 == 0:
        hailstone = hailstone // 2

    else:
        hailstone = (hailstone * 3) + 1

    print(hailstone)

    i += 1
