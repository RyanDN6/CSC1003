#!/usr/bin/env python3

s = input()

i = 0
ch = s[i]

while not (ch >= "a" and ch <= "g"):
    i += 1
    ch = s[i]

print(ch)
