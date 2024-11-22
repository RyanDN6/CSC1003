#!/usr/bin/env python3

import sys

with open("translation.txt", "r") as f:
    translations = f.readlines()

translate = {}

i = 0
while i < len(translations):
    translation = translations[i].strip().split()
    translate[translation[0]] = translation[1]
    i = i + 1

words = sys.stdin.readlines()

i = 0
while i < len(words):
    print(translate[words[i].strip()])
    i = i + 1
