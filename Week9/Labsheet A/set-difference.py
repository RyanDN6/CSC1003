#!/usr/bin/env python3

seenA = {}
seenB = {}

with open("a.txt", "r") as f:
    wordsA = f.readlines()

with open("b.txt", "r") as f:
    wordsB = f.readlines()

i = 0
while i < len(wordsA):
    word = wordsA[i].strip()
    if word not in seenA:
        seenA[word] = True
    i = i + 1

i = 0
while i < len(wordsB):
    word = wordsB[i].strip()
    if word not in seenB:
        seenB[word] = True
    i = i + 1

for key in seenA:
    if key not in seenB:
        print(key)
