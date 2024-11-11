#!/usr/bin/env python3

numbers = [0] * 1000

s = input()
while s != "end":
    numbers[int(s)] += 1
    s = input()

i = 0
while i < len(numbers):
    if numbers[i] != 0:
        print((str(i) + "\n") * (numbers[i] - 1), end="")
        print(i)

    i = i + 1
