import sys

if len(sys.argv) - 1 == 1:
    x = sys.argv[1]
    if x.count('z') > 0:

        for i in x:
            if i == 'z':
                print('z',end='')
        print()        
    else:
        print("none")
else:
    print("none")