#!/usr/bin/env python3

s = input()
out = ""

i = 0
while i < len(s):

    if "0" <= s[i] <= "9":
        out = s[i]

    i = i + 1

if out != "":
    print(out)
