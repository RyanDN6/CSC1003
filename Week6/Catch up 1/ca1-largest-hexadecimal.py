#!/usr/bin/env python3

n = input()
m = input()

digits = "0123456789abcdef"

if len(n) > len(m):
    print(n)

elif len(n) < len(m):
    print(m)

else:
    i = 0
    while i < len(n) and n[i] == m[i]:
        i = i + 1

    val1 = n[i]
    val2 = m[i]

    i = 0
    while digits[i] != val1:
        i = i + 1

    j = 0
    while digits[j] != val2:
        j = j + 1

    if i < j:
        print(m)
    else:
        print(n)
