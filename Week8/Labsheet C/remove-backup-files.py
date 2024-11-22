#!/usr/bin/env python3

import os
files = os.listdir(".")

i = 0
while i < len(files):
    if files[i][0] != "." and files[i][-4:] == ".bak":
        if os.path.isfile(files[i]):
            os.unlink(files[i])

    i = i + 1
