#!/usr/bin/env python3

jobs = []

s = input()
while s != "end":
    jobs.append(int(s))
    s = input()

maxServers = 0

i = 0
while i < len(jobs):
    j = i + 1
    while j < len(jobs) and jobs[j] < jobs[i] + 1000:
        j = j + 1

    servers = j - i
    if servers > maxServers:
        maxServers = servers

    i = i + 1

print(maxServers)
