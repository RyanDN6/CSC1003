#!/usr/bin/env python3

s = input()
sum = 0

i = 0
while i < 5:

    j = 0
    while j < len(s) and s[j] != "+":
        j = j + 1

    n = int(s[:j])
    s = s[j + 1:]

    sum += n

    i = i + 1

print(sum)
