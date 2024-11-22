#!/usr/bin/env python3

import sys

factors = sys.argv[1:]
numbers = sys.stdin.readlines()

i = 0
while i < len(numbers):
    n = int(numbers[i].strip())
    check = True

    j = 0
    while j < len(factors):
        if n % int(factors[j]):
            check = False
        j = j + 1

    if check:
        print(n)
    i = i + 1
