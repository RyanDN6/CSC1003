#!/usr/bin/env python3

import sys
minimum = 100

a = int(input())
b = int(input())

if a < minimum or b < minimum:
   print("a and b must both be at least", minimum)
   #
   # sys.exit() causes the script to exit immediately.
   #
   sys.exit(1)

while 0 < b:
   print(f"r = {a} % {b} = {a % b}")
   r = a % b    # r = a % 7
   a = b        # a = 7
   b = r        # b = a % 7

print(a)        # 7

