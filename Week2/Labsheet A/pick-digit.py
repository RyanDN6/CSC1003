#!/usr/bin/env python3

n = int(input())
digit = int(input())

n = n % 10 ** (digit + 1)
n = n // 10 ** digit

print(n)
