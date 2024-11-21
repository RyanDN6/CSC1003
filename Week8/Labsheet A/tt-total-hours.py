#!/usr/bin/env python3

hours = 0

s = input()
while s != "end":
    hours += int(s.split()[2])
    s = input()

print(hours)
