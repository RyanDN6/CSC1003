#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:

    number = i + 1

    if number % 15 == 0:
        print("fizz-buzz")

    elif number % 5 == 0:
        print("buzz")

    elif number % 3 == 0:
        print("fizz")

    else:
        print(number)

    i += 1
