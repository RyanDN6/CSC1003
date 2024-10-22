#!/usr/bin/env python3

s = input()
out = ""

i = 0
while i < len(s):

    if "0" <= s[i] <= "9":
        j = i - 1
        while j >= 0 and "0" <= s[j] <= "9":
            j -= 1

        out = s[j + 1:i + 1]

    i = i + 1

if out != "":
    print(out)
