#!/usr/bin/env python3

dates = []

with open("irish-dobs.txt", "r") as f:
    irishDates = f.readlines()

i = 0
while i < len(irishDates):
    date = irishDates[i].strip().split("/")

    tmp = date[0]
    date[0] = date[1]
    date[1] = tmp

    dates.append("/".join(date))

    with open("american-dobs.txt", "w") as f:
        f.write("\n".join(dates) + "\n")

    i += 1
