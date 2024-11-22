#!/usr/bin/env python3

import sys

seen = {}

words = sys.stdin.readlines()

i = 0
while i < len(words):
    word = words[i].strip()
    if word in seen:
        seen[word] = False
    else:
        seen[word] = True
    i = i + 1

for key in seen:
    if seen[key] is True:
        print(key)
