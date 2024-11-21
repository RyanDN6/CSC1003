#!/usr/bin/env python3

s = input()
while s != "end":
    s = s.split()

    start = int(s[1]) % 24
    hours = int(s[2]) - 1

    end = (start + hours) % 24
    start = str(start) + ":00"
    s[1] = start
    end = str(end) + ":50"

    s[2] = end

    print(" ".join(s))

    s = input()
