#!/usr/bin/env python3

s = input()

i = 0
ch = s[i]

while not (ch >= "A" and ch <= "Z"):
    i += 1
    ch = s[i]

print(i)
