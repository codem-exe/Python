#Python Rock Paper Game:

import random

options = ("Rock","Paper","Scissors")

running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter Your Choice (Rock/Paper/Scissor): ").capitalize()


    print(f"Player: {player.capitalize()}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a Tie!")
    elif player == "rock" and computer == "scissors":
        print("You Won!")
    elif player == "paper" and computer == "rock":
        print("You Won!")
    elif player == "scissors" and computer == "paper":
        print("You Won!")
    else:
        print("You Lose!")

    if not input("Wanna Play Again ? ").lower() == "y":
        running = False

print("Thanks For Playing!!")