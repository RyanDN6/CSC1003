#!/usr/bin/env python3

s = input()

if s[0] == ".":
    print("0" + s)
elif s[:2] == "-.":
    print(s[0] + "0" + s[1:])
elif s[-1] == ".":
    print(s + "0")
else:

    i = 0
    while i < len(s) and s[i] != ".":
        i = i + 1

    if i < len(s):
        print(s)
    else:
        print(s + ".0")
