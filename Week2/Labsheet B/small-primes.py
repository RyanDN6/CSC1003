#!/usr/bin/env python3

n = int(input())

if n == 1 or n == 4:
    print("not prime")
elif n <= 5:
    print("prime")
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
    print("not prime")
else:
    print("prime")
