first_number = float(input("Enter your first number :"))
second_number = float(input("Enter your second number :"))

operator = input("Enter operator:")
try:
    if operator == "+":
        result = first_number + second_number

    elif operator == "-":
        result = first_number - second_number

    elif operator == "/":
        result = first_number/second_number
    
    elif operator == "*":
        result = first_number * second_number

    else:
        print("invalid operator")

    print(result)

   
except ZeroDivisionError as e:
    print("can't divide by zero")
