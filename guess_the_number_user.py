import random

def computer_guess(n):
    low = 1
    high = n
    feedback = ''    

    while feedback != 'c':
        if(low != high):
            random_number = random.randint(low, high)
        else:
            random_number = low
        print(f"Correct number is {random_number} ??")
        feedback = input("Please confirm - c for correct,  h for too high, l for too low : ").lower()

        if feedback == 'h':
            high = random_number - 1
        elif feedback == 'l':
                low = random_number + 1


    print("Yay, I guessed it right.")


computer_guess(10)