import sys
x = len(sys.argv)-1
i=1
if x==0 or x>2:
    print("none")
else:
    for i in sys.argv[1:]:
        num1=int(sys.argv[1])
        num2=int(sys.argv[2])
        if num1<num2:
            series = list(range(num1, num2+1))
            print(series)
        else:
            print("The first number is bigger than the second number.\nSwitch them now! Do it right, bro.\nWhy did you do such a thing?\nIt's okay, I'm just joking, but seriously,\ndo it right.")
        break