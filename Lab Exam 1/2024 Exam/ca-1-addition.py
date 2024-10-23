#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and s[i] != " ":
    i = i + 1

number1 = int(s[:i])
s = s[i + 1:]

j = 0
while j < len(s) and s[j] != " ":
    j = j + 1

number2 = int(s[:j])
number3 = int(s[j + 1:])

print(number1 + number2 + number3)
