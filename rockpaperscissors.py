import random
computer = random.choice(["rock", "paper", "scissors"])

player = input("Do you want rock, paper, or scissors?\n")

if computer == player:
    print("Computer chose: " + str(computer))
    print("You chose: " + str(player))
    print("It's a tie!")
elif (computer == "rock" and player == "scissors") or (computer == "paper" and player == "rock") or (computer == "scissors" and player =="paper"):
    print("Computer chose: " + str(computer))
    print("You chose: " + str(player))
    print("You lose!")
else:
    print("Computer chose: " + str(computer))
    print("You chose: " + str(player))
    print("You win!")
