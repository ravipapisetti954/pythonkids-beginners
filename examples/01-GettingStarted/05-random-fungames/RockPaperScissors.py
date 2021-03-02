import random
choices = ["rock", "paper", "scissors"]

print("Rock crushes scissors, Scissors cut paper, Paper covers rock.")
player = input("Do you want to be rock, paper, or scissors (or quit)?")

while player != "quit":
    player = player.lower()
    computer = random.choice(choices)
    print("You choose "+ player + ", and the computer chose "+computer+".")

    if player == computer:
        print("It is a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You WIN!")
        else:
            print("Computer WINS!")
    elif player == "scissors":
        if computer == "paper":
            print("You WIN!")
        else:
            print("Computer WINS!")
    elif player == "paper":
        if computer == "rock":
            print("You WIN!")
        else:
            print("Computer WINS!")
    else:
        print("I think you choose an incorrect choice")
    print()
    player = input("Do you want to be rock, paper, or scissors (or quit)?")
    
