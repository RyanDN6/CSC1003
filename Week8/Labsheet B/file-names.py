#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    print(lines[i].strip().split("/")[-1])
    i += 1
