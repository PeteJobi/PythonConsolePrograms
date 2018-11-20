def rps(p1Choice, p2Choice):
    if p1Choice == p2Choice:
        print("It's a tie")
    elif p1Choice not in ["rock", "paper", "scissors"] or p2Choice not  in ["rock", "paper", "scissors"]:
        print("There's an invalid input")
    elif (p1Choice == "rock" and p2Choice == "scissors" or
        p1Choice == "scissors" and p2Choice == "paper" or
        p1Choice == "paper" and p2Choice == "rock"):
        print("Player 1 wins")
    else:
        print("Player 2 wins")


replay = "y"
while (replay is "y"):
    rps(input("\nPlease enter a choice, player 1:").lower(), input("Please enter a choice, player 2:").lower())
    replay = input("Do you want to retry? Enter 'y' to retry.\n")

