import random 

secret_number = random.randint(1,10)

attempts = 0

while True:
    
    guess_number = int(input("Enter your number :"))
    if guess_number > secret_number:
        print("Entered number is high..")
    elif guess_number < secret_number:
        print("Entered number is Low..")
    else:
        print("The Number You Are Guessing Is Right..")
        break
    attempts += 1
   
        

print("GAME OVER !")
print(f"You Win The Game In {attempts} Attempt.")
