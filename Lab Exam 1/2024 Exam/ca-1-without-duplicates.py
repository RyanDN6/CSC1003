#!/usr/bin/env python3

prev = int(input())
print(prev)

i = 0
while i < 9:
    curr = int(input())
    if curr != prev:
        print(curr)
    prev = curr
    i = i + 1
