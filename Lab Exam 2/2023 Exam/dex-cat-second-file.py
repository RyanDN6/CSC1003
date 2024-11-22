#!/usr/bin/env python3

import sys

file1 = sys.argv[1]

with open(file1, "r") as f:
    file2 = f.read().strip()

with open(file2, "r") as f:
    print(f.read().strip())
