import sys
x = len(sys.argv)-1
if x!=1:
    print("none")
else:
    print(sys.argv[1].lower())
