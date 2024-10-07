#!/usr/bin/env python3

length = int(input())

i = 0
while i < length:

    if i == length // 2:
        print(" " * (length // 2) + "*")
    elif i < length // 2:
        print(" " * i + "*" + " " * (length - (2 * i) - 2) + "*")
    else:
        j = length - i - 1
        print(" " * j + "*" + " " * (length - (2 * j) - 2) + "*")

    i = i + 1
