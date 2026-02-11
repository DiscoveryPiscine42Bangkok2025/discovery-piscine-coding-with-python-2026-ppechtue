import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    x = sys.argv[1]
    y = sys.argv[2]
    
    z = re.findall(x, y)
    
    count = len(z)
    
    if count > 0:
        print(count)
    else:
        print("none")