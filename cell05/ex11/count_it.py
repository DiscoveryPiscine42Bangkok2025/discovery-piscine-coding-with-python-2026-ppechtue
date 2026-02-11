#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
else:
    x = len(sys.argv) - 1
    print(f"parameters: {x}")
    y = sys.argv[1:]

    for i in y:
        print(f"{i}: {len(i)}")