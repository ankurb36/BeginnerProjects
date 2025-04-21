import random

def guess(x):
    random_number = random.randint(1,x)   
    guess_number = 0 

    while guess_number != random_number:
        guess_number = int(input("Guess the number: "))
        if guess_number < random_number:
            print("Correct answer is greater than your guess.")
        elif guess_number > random_number:
            print("Correct answer is smaller than your guess.")   

    print("Bingo!, you guessed it right.") 

guess(100)