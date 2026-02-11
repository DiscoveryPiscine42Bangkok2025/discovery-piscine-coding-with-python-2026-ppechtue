#!/usr/bin/env python3
import sys

if len(sys.argv) - 1 != 2:
    print("none")
else:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    
    num = range(x, y + 1)
    
    z = list(num)
    
    print(z)