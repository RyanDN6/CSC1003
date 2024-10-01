#!/usr/bin/env python3

first = int(input())
length = len(str(first))

total = first

second = 0

i = 0
while i < length:
    digit = total % 10
    second += digit * (10 ** (length - 1 - i))

    total //= 10
    i += 1

if first == second:
    print("yes")
else:
    print("no")
