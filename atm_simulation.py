balance = 5000

while True:
    print("== Machine Started...")

    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")


    Choice = input("Enter your choice :")

    if Choice == "1":
        print(f"your balance is {balance}")

    elif Choice == "2":
        amount = float(input("Enter your deposit ammount :"))
        balance += amount
        print(f"Now your total amount is {balance}")

    elif Choice == "3":
        amount = float(input("Enter your deposit ammount :"))

        if balance < amount:
            print("Insufficient  balance.")

        else:
            balance -= amount
            print("Please collect your cash.")
            print(f"Remaining amount  is {balance}")

    elif Choice == "4":
        print("Thanks for using the ATM")
        break

    else:
        print("invalid choice ")
        


