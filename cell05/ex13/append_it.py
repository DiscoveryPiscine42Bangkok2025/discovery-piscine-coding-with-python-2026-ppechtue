#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
else:
    params = sys.argv[1:]
    
    for param in params:
        
        if not param.endswith("ism"):
            
            print(f"{param}ism")