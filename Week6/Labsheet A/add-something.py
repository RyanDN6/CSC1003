#!/usr/bin/env python3

a = []
s = input()

while s != "end":
    a.append(int(s))
    s = input()

add = int(input())

i = 0
while i < len(a):
    print(a[i] + add)
    i = i + 1
