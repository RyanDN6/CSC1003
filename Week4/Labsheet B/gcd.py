#!/usr/bin/env python3

a = int(input())
b = int(input())

while b != 0:
    tmp = a % b
    a = b
    b = tmp

print(a)
