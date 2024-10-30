#!/usr/bin/env python3

count = 0

s = input()
while s != "end":

    i = 0
    while i < len(s) and s[i] != ",":
        i = i + 1

    state = s[i + 1: i + 3]

    if state == "WI":
        count += 1

    s = input()

print(count)
