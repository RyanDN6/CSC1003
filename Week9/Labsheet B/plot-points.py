#!/usr/bin/env python3

import sys

matrix = []

matrix.append([" "] + (["-"] * 20))

i = 0
while i < 20:
    a = ["|"] + ([" "] * 20) + ["|"]
    matrix.append(a)
    i = i + 1

matrix.append([" "] + (["-"] * 20))

points = sys.stdin.readlines()


i = 0
while i < len(points):
    x, y = map(int, points[i].strip().split())
    matrix[20 - y][x + 1] = "*"
    i = i + 1

i = 0
while i < len(matrix):
    print("".join(matrix[i]))
    i = i + 1
