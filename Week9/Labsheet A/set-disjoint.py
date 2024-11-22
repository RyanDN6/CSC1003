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

disjoint = True

dataA = seenA.keys()
dataB = seenB.keys()
i = 0
while i < len(dataA):
    if dataA[i] in dataB:
        disjoint = False
    i = i + 1

if disjoint:
    print("disjoint")
else:
    print("intersecting")
