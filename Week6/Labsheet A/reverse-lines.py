#!/usr/bin/env python3

a = []
s = input()

while s != "end":
    a.append(s)
    s = input()

length = len(a)

i = 0
while i < length:
    print(a[length - 1 - i])
    i = i + 1
