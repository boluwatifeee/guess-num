
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Your guess is lower than the number")
        elif guess > random_number:
            print("Your guess is higher than number")
    
    print("You guessed right!")
    
guess(5)
            
    