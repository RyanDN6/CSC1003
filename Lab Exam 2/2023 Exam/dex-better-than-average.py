#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

total = 0
names = {}

i = 0
while i < len(lines):
    line = lines[i].strip().split()

    name = " ".join(line[:2])
    mark = int(line[2])
    names[name] = mark

    total += mark
    i += 1

average = total // len(lines)

keys = list(names.keys())

i = 0
while i < len(names):
    if names[keys[i]] > average:
        print(keys[i])
    i = i + 1
