#!/usr/bin/env python3

length = int(input())

i = 0
while i < length:
    if i == 0 or i == length - 1:
        print("*" * length)
    else:
        print("*" + (" " * (length - 2)) + "*")
    i = i + 1
