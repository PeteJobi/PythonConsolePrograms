def printBoard(tiles):
    for i in range(tiles):
        for j in range(tiles):
            print(" ---", end="")
        print("\n")
        for j in range(tiles):
            print("|   ", end="")
        print("|\n")
    for i in range(tiles):
        print(" ---", end="")

tiles = int(input("What size would you like for your dumbass board?\n"))
printBoard(tiles)