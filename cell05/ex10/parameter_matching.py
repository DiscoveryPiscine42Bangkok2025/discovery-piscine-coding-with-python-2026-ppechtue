#!/usr/bin/env python3
import sys

if len(sys.argv) - 1 == 1:
    x = sys.argv[1]
    y = input("What was the parameter? ")
    
    if y == x:
        print("Good job!")
    else:
        print("Nope, sorry...")
        
else:
    print("none")