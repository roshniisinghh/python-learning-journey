num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
operation = input("Choose (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 == 0:
        print ("ERROR A NUMBER CANNOT BE DIVIDED BY ZERO")
    else:
        print(num1/num2)
else:
    print("CHOOSE VALID OPERATOR")