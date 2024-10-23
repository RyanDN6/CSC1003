#!/usr/bin/env python3

s = input()
while s != "end":

    i = 1
    while i < len(s) and s[i - 1] <= s[i]:
        i = i + 1

    if i == len(s):
        print(s)

    s = input()
