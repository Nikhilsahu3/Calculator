print("Calculator\n")

operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
        exit()
    result = num1 / num2
else:
    print("Invalid operator")
    exit()

print("Result: ", result)
