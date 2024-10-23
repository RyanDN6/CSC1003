#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
r = int(input())
x2 = int(input())
y2 = int(input())

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if distance < r:
    print("yes")
else:
    print("no")
