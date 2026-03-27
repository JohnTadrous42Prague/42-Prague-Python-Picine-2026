import sys
x = len(sys.argv)-1
print("parameters: ",x)
i=1
for i in sys.argv[1:]:
    print(i,": ",len(i))
