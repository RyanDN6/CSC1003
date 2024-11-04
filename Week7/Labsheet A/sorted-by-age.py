#!/usr/bin/env python3

dates = []
people = []

s = input()

while s != "end":
    n = int(s[6:8] + s[3:5] + s[0:2])
    dates.append(n)
    people.append(s[9:])
    s = input()

i = 0
while i < len(dates) - 1:
    j = i + 1
    p = i
    while j < len(dates):
        if dates[j] < dates[p]:
            p = j
        j = j + 1

    tmp = dates[p]
    dates[p] = dates[i]
    dates[i] = tmp

    tmp = people[p]
    people[p] = people[i]
    people[i] = tmp

    i = i + 1

i = 0
while i < len(people):
    print(people[i])
    i = i + 1
