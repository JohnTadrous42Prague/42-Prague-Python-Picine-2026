import sys
x = len(sys.argv)-1

if x<3:
    print("none")
else:
    for i in reversed(sys.argv):
        print(i)
