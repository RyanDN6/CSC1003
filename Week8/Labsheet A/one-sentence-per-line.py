#!/usr/bin/env python3

lines = []
s = input().strip()
while s != "end":
    lines.append(s)
    s = input().strip()

text = " ".join(" ".join(lines).split()).split(".")

i = 0
while i < len(text):
    sentence = text[i].strip()

    if sentence:
        print(sentence + ".")

    i = i + 1
