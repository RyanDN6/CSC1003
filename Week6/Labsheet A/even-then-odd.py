#!/usr/bin/env python3

a = []
s = input()

while s != "end":
    s = int(s)

    if s % 2 == 0:
        print(s)
    else:
        a.append(int(s))

    s = input()

i = 0
while i < len(a):
    print(a[i])
    i = i + 1
