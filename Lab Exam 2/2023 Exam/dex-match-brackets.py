#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
brackets = {
    "(": ")",
    "[": "]",
    "{": "}"
}

i = 0
while i < len(lines):
    line = lines[i]
    j = 0
    stack = []
    error = ""

    while j < len(line):
        ch = line[j]
        if ch in brackets.keys():
            stack.append(ch)
        elif ch in brackets.values():
            if len(stack) > 0:
                if brackets[stack[len(stack) - 1]] == ch:
                    stack.pop()
                else:
                    if error == "":
                        error = str(i) + " " + str(j)
            else:
                if error == "":
                    error = str(i) + " " + str(j)
        j = j + 1

    if error == "" and len(stack) > 0:
        if error == "":
            error = str(i) + " " + str(j - 1)

    if error != "":
        print(error)

    i = i + 1
