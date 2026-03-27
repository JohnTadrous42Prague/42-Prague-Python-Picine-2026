try:
    Number=int(input("Enter a number: "))
    i=0

    while i <= Number:
        result = i*Number
        print(i," X ",Number," = ",result)
        i+=1

except:
    print("ERROR!")