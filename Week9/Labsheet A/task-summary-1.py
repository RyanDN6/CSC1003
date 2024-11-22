#!/usr/bin/env python3

import sys

files = sys.stdin.readlines()

tasks = {}

i = 0
while i < len(files):
    file = files[i].strip().split(".")
    tasks[".".join(file[:-1])] = file[-1]
    i = i + 1

for key in tasks:
    if tasks[key] == "correct":
        print(key)
