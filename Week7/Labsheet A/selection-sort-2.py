#!/usr/bin/env python3

a = []
s = input()

while s != "end":
    a.append(int(s))
    s = input()

j = int(input())
smallest = a[j]
p = j

i = j + 1
while i < len(a):
    if a[i] < smallest:
        smallest = a[i]
        p = i

    i = i + 1

print(p)
