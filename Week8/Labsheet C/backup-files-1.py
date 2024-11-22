#!/usr/bin/env python3

import os
files = os.listdir(".")

i = 0
while i < len(files):
    if files[i][0] != "." and files[i].split(".")[-1] != "bak":
        backup = files[i] + ".bak"
        with open(files[i], "r") as f:
            data = f.read()

        with open(backup, "w") as f:
            f.write(data)

    i = i + 1
