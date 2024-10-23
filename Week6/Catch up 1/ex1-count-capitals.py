#!/usr/bin/env python3

count = 0
s = input()

i = 0
while i < len(s):

    if "A" <= s[i] <= "Z":
        count += 1

    i = i + 1

print(count)
