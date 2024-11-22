#!/usr/bin/env python3

import sys

boys = {}
girls = {}
either = {}

with open("boys.txt", "r") as f:
    boyNames = f.readlines()

with open("girls.txt", "r") as f:
    girlNames = f.readlines()

i = 0
while i < len(boyNames):
    word = boyNames[i].strip()
    boys[word] = True
    i = i + 1

i = 0
while i < len(girlNames):
    word = girlNames[i].strip()
    girls[word] = True
    if word in boys:
        either[word] = True
    i = i + 1

names = sys.stdin.readlines()

i = 0
while i < len(names):
    name = names[i].strip()
    if name in either:
        print(name, "either")
    else:
        if name in boys:
            print(name, "boy")
        else:
            print(name, "girl")
    i = i + 1
