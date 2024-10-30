#!/usr/bin/env python3

import sys

grep = sys.argv[1]
length = len(grep)

s = input()
while s != "end":
    hit = False

    i = 0
    while i <= len(s) - len(grep):

        if s[i] == grep[0]:
            word = s[i:i + len(grep)]
            if word == grep:
                hit = True

        i = i + 1

    if hit:
        print(s)

    s = input()
