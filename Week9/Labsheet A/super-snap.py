#!/usr/bin/env python3

import sys

seen = {}

words = sys.stdin.readlines()

i = 0
while i < len(words):
    word = words[i].strip()
    if word in seen:
        print("snap:", word)
        i = len(words)
    else:
        seen[word] = True
    i = i + 1
