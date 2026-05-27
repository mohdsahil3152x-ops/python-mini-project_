
import math

print("==CALCULATOR==")
print("1-basic level")
print("2-advance level")

option = input("SELECT YOUR OPTION :")
try:
    if option == "1":
        first_number = float(input("Enter your first number :"))
        second_number = float(input("Enter your second number :")) 
        operator = input("Enter Your Operator :")

        if operator == "+":
            result = first_number + second_number
            print(result)

        elif operator == "-":
            result = first_number - second_number
            print(result)

        elif operator == "/":
            result = first_number/second_number
            print(result)
        
        elif operator == "*":
            result = first_number * second_number
            print(result)

        else:
            print("invalid operator")

        

    elif option == "2":
        print("s-SquareRoot")
        print("f-Factorial")
        print("p-Power")
        options = input("SELECT YOUR OPTION :")

        # number = float(input("Enter your number :"))

        if options == "s":
            number = float(input("Enter your number :"))
            print(f"Square root of your number is {math.sqrt(number)}")

        elif options == "f":
            number = int(input("Enter your number :"))
            print(f"Factorial of your number is {math.factorial(number)}")

        elif options == "p":
            base_number = float(input("enter a base number :"))
            power_number = float(input("enter a power number :"))
            print(f"power of your number is {math.pow(base_number,power_number)}")

        else:
            print("invalid options")

    else:
        print("No More Options Available ...")

except ZeroDivisionError as e :
    print("Can't divide by zero")