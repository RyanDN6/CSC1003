#!/usr/bin/env python3

s = input()

out = ""
i = 0
while i < len(s):
    if s[i] != " ":
        out += s[i]

    i = i + 1

print(out)
