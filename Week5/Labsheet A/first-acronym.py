#!/usr/bin/env python3

s = input()

i = 0

while i < len(s) and not ("A" <= s[i] <= "Z"):
    i = i + 1

if i < len(s):
    s = s[i:]

    j = 0

    while j < len(s) and "A" <= s[j] <= "Z":
        j = j + 1

    print(s[:j], i)
