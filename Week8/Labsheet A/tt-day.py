#!/usr/bin/env python3

timetable = []

s = input()
while s != "end":
    timetable.append(s)
    s = input()

day = input()

i = 0
while i < len(timetable):
    if timetable[i].split()[0] == day:
        print(timetable[i])
    i = i + 1
