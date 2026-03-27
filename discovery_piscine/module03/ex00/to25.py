try:
    Number=int(input("Enter a number less than 25: "))
    if Number<=25:
        i = 25
        while i >= Number:
            print(f"Inside the loop, my variable is {Number}")
            Number+=1
    else:
        print("Error")
except:
    print("ERROR")