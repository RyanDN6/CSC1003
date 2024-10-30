#!/usr/bin/env python3

n = m = 0

while n + m != 1000:
    s = input()

    j = 0
    while j < len(s) and s[j] != "+":
        j = j + 1

    n = int(s[:j])
    m = int(s[j + 1:])

    print(n + m)
