#!/usr/bin/env python3

month = int(input()) - 1
days = int(input())

day = (month * 30) + days

print(((day - 1) % 7) + 1)
