#Take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#Comapare the numbers
if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print (num1, "is smaller than", num2)
else:
    print("both numbers are equal")
