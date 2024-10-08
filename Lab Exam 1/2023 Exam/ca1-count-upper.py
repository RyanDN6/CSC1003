#!/usr/bin/env python3

s = input()

upper = 0
i = 0
while i < len(s):
    ch = s[i]
    if ch >= "A" and ch <= "Z":
        upper += 1

    i += 1

print(upper)
