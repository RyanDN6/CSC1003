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

weight = 0

i = 0
while i < len(a) and weight + a[i] <= 500:
    weight += a[i]
    i = i + 1

print(i, weight)
