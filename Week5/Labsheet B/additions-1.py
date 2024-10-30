#!/usr/bin/env python3

i = 0
while i < 10:
    s = input()

    j = 0
    while j < len(s) and s[j] != "+":
        j = j + 1

    n = int(s[:j])
    m = int(s[j + 1:])

    print(n + m)

    i = i + 1
