#!/usr/bin/env python3

numbers = input()

while numbers != "end":

    n = ""
    m = ""

    i = 0
    while numbers[i] != " ":
        n += numbers[i]
        i = i + 1

    n = int(n)
    m = int(numbers[i + 1:])
    answer = str(n + m)

    numbers = str(n) + " + " + str(m)
    spaces = 21 - len(numbers) - 2

    print(" " * spaces + numbers + " = " + answer)

    numbers = input()
