#!/usr/bin/env python3

p = int(input())
c = int(input())

while (p % 2 == 0 and c != p // 2) or (p % 2 == 1 and c != p * 3 + 1):
    p = c
    c = int(input())

print(p, c)
