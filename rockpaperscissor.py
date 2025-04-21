import random

def play():
    user = input("Enter your choice - r for rock, p for paper, s for scrissor: \n").lower()
    computer = random.choice(['r', 'p', 's']).lower()

    if user == computer:
        print("It's a tie.")
    elif is_win(user, computer):
        print("You won!")
    else:
        print("You lost.")

    print(f"computer: {computer}")



def is_win(usr, comp):
    if(usr == 'r' and comp == 's') or (usr == 's' and comp == 'p') or (usr == 'p' and comp == 'r'):
        return True
    
    return False

while 1 != 2:
    play()
