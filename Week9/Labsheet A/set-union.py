#!/usr/bin/env python3

seen = {}

with open("a.txt", "r") as f1, open("b.txt", "r") as f2:
    words = f1.readlines() + f2.readlines()


i = 0
while i < len(words):
    word = words[i].strip()
    if word not in seen:
        seen[word] = True
    i = i + 1

for key in seen:
    print(key)
