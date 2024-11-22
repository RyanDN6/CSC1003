#!/usr/bin/env python3

import os

filename = "start.txt"

while os.path.isfile(filename):
    with open(filename, "r") as f:
        filename = f.read().strip()

print(filename)
