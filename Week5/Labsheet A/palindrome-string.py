#!/usr/bin/env python3

s = input()

start = 0
end = len(s) - 1

while start <= len(s) // 2 and s[start] == s[end]:
    start += 1
    end -= 1

if start > len(s) // 2:
    print("palindrome")
