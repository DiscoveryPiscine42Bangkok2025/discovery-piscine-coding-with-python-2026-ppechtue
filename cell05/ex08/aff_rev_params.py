#!/usr/bin/env python3
import sys

params = sys.argv[1:]

if len(params) < 2:
    print("none")
else:
    for word in reversed(params):
        print(word)
