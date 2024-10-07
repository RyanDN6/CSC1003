#!/usr/bin/env python3

s = input()

out = ""
i = 0
while i < len(s):
    out += (s[len(s) - i - 1])
    i = i + 1

print(out)
