#!/usr/bin/env python3

s = input()
while s != "end":

    i = 0
    while i < len(s) and s[i] != ",":
        i = i + 1

    city = s[i - 4:i]

    if city == "City" and len(s[:i]) != 4:
        print(s[:i])

    s = input()
