#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

sum = 0

i = 0
while i < len(lines):
    sum += int(lines[i].strip())
    i += 1

print(sum)
