#!/usr/bin/env python3

s = input()

out = ""
i = 0
while i < len(s):
    ch = s[i]

    if ch >= "a" and ch <= "z":
        ch = chr(ord(ch) - 32)

    out += ch

    i = i + 1

print(out)
