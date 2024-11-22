#!/usr/bin/env python3

import sys

redcated = sys.argv[1:]

words = sys.stdin.readlines()

i = 0
while i < len(words):
    word = words[i].strip()
    if word in redcated:
        print("*" * len(word))
    else:
        print(word)
    i = i + 1
