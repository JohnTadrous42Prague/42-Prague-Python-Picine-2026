import sys
x = len(sys.argv)-1

if x==1:
    y = input("What was the parameter? ")
    if y==sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
elif x!=1:
    print("none")
else:
    print