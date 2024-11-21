#!/usr/bin/env python3

import sys

files = sys.argv[1:]

sum = 0
file = 0

while file < len(files):
    with open(files[file], "r") as f:

        lines = f.readlines()

        i = 0
        while i < len(lines):
            sum += int(lines[i].strip())
            i += 1

    file += 1

print(sum)
