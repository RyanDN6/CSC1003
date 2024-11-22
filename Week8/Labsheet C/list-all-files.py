#!/usr/bin/env python3

import os

directories = ["."]
root = ""

while len(directories) > 0:
    directory = directories.pop(0)
    files = os.listdir(directory)
    root = directory + "/"

    i = 0
    while i < len(files):
        full_path = root + files[i]

        if os.path.isfile(full_path):
            print(full_path)
        elif os.path.isdir(full_path) and files[i] not in [".", ".."]:
            directories.append(full_path)
        i = i + 1
