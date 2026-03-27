FirstNumber=float(input("Enter the first number: "))
SecondNumber=float(input("Enter the second number: "))

number= FirstNumber * SecondNumber
print(FirstNumber," X ",SecondNumber," = ",number)
if number < 0:
    print("The result is negative.")
elif number > 0:
    print("The result is positive.")
else:
    print("The result is both positive and negative.")
