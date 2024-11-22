#!/usr/bin/env python3

import os
files = os.listdir(".")

i = 0
while i < len(files):
    if files[i][0] != "." and files[i].split(".")[-1] == "py":
        with open(files[i], "r") as f:
            if f.read():
                print(files[i])
    else:
        with open(files[i], "r") as f:
            if f.readline() == "#!/usr/bin/env python3\n":
                print(files[i])
    i = i + 1
