#!/usr/bin/env python3

import sys

url = sys.argv[1]

url = url.split(":")
print("scheme: " + url[0])
print("host: " + url[1].split("/")[2])
if len(url) > 2:
    print("port: " + url[2].split("/")[0])

url = "".join(url).split("/")[2:-1]

fragment = False
query = False

url = url.split("#")
if len(url) > 1:
    fragment = True
    fragPrint = "fragment-id: " + url[1]
    url = url[0]
else:
    url = "".join(url)

url = url.split("?")
if len(url) > 1:
    query = True
    queryPrint = "query-string: " + url[1]
    url = url[0]
else:
    url = "".join(url)

print("path: /" + url)

if query:
    print(queryPrint)
if fragment:
    print(fragPrint)
