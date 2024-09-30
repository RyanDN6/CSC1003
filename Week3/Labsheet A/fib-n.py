#!/usr/bin/env python3

n = int(input())

prev = 0
curr = 1

i = 0
while i < n:

    print(prev)

    tmp = prev
    prev = curr
    curr += tmp

    i = i + 1
