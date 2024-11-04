#!/usr/bin/env python3

a = []
s = input()

while s != "end":
    a.append(int(s))
    s = input()

i = 0
while i < len(a) - 1:
    j = i + 1
    p = i
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1

    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp

    i = i + 1

i = 0
while i < len(a):
    print(a[i])
    i = i + 1
