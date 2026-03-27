import sys
x = len(sys.argv)-1
i=1
if x==0:
    print("none")
else:
    for i in sys.argv[1:]:
        if "ism" not in i:
            print(i+"ism")
