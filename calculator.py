num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))
operation = input("Choose (+, -, *, /): ")

if operation == "+":
    print("Sum is",num1 + num2)
elif operation == "-":
    print("Difference is",num1 - num2)
elif operation == "*":
    print("Product is",num1 * num2)
elif operation == "/":
    if num2 == 0:
        print ("ERROR A NUMBER CANNOT BE DIVIDED BY ZERO")
    else:
        print("Quotient is",num1/num2)
else:
    print("CHOOSE VALID OPERATOR")