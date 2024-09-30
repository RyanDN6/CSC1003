#!/usr/bin/env python3

n = int(input())

prev = 0
curr = 1

while prev < n:

    print(prev)

    tmp = prev
    prev = curr
    curr += tmp
