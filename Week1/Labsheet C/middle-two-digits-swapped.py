#!/usr/bin/env python3

n = int(input())  # eg. n = 876345

n = n // 100      # n = 8763

n = n % 100       # n = 63

a = n % 10        # a = 3

b = n // 10       # a = 6

a = a * 10        # a = 30

print(a + b)      # = 30 + 6 --> 36
