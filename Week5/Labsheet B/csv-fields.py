#!/usr/bin/env python3

s = input()
boolean = True

while boolean:

    j = 0
    while j < len(s) and s[j] != ",":
        j = j + 1

    header = s[:j]
    print(header)

    if j < len(s):
        s = s[j + 1:]
    else:
        boolean = False
