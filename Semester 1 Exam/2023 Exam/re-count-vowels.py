#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
vowels = "aeiouAEIOU"
count = 0

i = 0
while i < len(lines):
    line = lines[i].strip()
    j = 0
    while j < len(line):
        ch = line[j]
        if ch in vowels:
            count += 1
        j += 1
    i += 1

print(count)
