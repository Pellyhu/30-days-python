#advanced_calculator
import math

print("Welcome to Python Calculator! ")
print ("Available operations: +,-,*,/,^,%,sqrt,quit")

while True:
    operator = input("\nEnter operator ( +,-,*,/,^,%,sqrt,quit): ")

    if operator == "quit":
        print("Exiting Calculator... Goodbye!")
        break #stop the loop

    if operator == "sqrt":
        num = float(input("Enter number: "))
        result = math.sqrt(num)
        print("Result: ", result)
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1/num2
            else:
                result = "Error!, Division by zero"
        elif operator == "^":
            result = num1 ** num2
        elif operator == "%":
            result = num1 % num2
        else:
            result = "Invalid Operator!"

        print("Result: ", result)
