#!/usr/bin/env python3

import sys

files = sys.stdin.readlines()

users = {}

i = 0
while i < len(files):
    data = files[i].strip().split("/")
    user = data[0]

    if user not in users:
        users[user] = {}

    file = data[1].split(".")

    taskname = ".".join(file[:-1])
    test = file[-1]

    users[user][taskname] = test

    i = i + 1

total = 0
for user in users:
    for key in users[user]:
        if users[user][key] == "correct":
            total += 1
    print(user, total)
    total = 0
