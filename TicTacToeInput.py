board = [[0,0,0],[0,0,0],[0,0,0]]
displayBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]

for i in range(9):
    while True:
        tile = input(f"Player {(i % 2) + 1}, please input a tile in the form of x,y\n")
        x, y = int(tile[0]), int(tile[-1])
        if board[x - 1][y - 1] is 0:
            board[x - 1][y - 1] = (i % 2) + 1
            displayBoard[x - 1][y - 1] = 'X' if (i % 2) + 1 is 1 else 'O'
            break
        else:
            print(f"Tile {tile} is already taken. Please try again.\n")

    for j in displayBoard:
        print(j)
    print("\n")