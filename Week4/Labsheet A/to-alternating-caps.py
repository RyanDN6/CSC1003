#!/usr/bin/env python3

s = input()

out = ""
alt = 0
i = 0
while i < len(s):
    ch = s[i]

    if (ch >= "a" and ch <= "z"):

        if alt % 2 == 1:
            ch = chr(ord(ch) - 32)
        alt += 1

    elif (ch >= "A" and ch <= "Z"):

        if alt % 2 == 0:
            ch = chr(ord(ch) + 32)

        alt += 1

    out += ch

    i = i + 1

print(out)
