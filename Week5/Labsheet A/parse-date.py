#!/usr/bin/env python3

s = input()

i = 0

while i < len(s) and s[i] != " ":
    i = i + 1

day = s[:i]

s = s[i + 1:]

i = 0
while i < len(s) and s[i] != " ":
    i = i + 1

date = s[:i]

s = s[i + 1:]

i = 0
while i < len(s) and s[i] != ",":
    i = i + 1

month = s[:i]

year = s[i + 2:]

print(month, date + ",", year, "(" + day + ")")
