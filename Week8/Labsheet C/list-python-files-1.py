#!/usr/bin/env python3

import os
files = os.listdir(".")         # Line A.

i = 0
while i < len(files):
    if files[i][0] != "." and files[i].split(".")[-1] == "py":       # Line B.
        print(files[i])
    i = i + 1
