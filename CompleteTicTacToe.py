def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(" ---", end="")
        print("\n")
        for j in range(3):
            print("| ", end="")
            if board[i][j] is 0:
                print("  ",end="")
            elif board[i][j] is 1:
                print("X ", end="")
            elif board[i][j] is 2:
                print("O ", end="")
        print("|\n")
    for i in range(3):
        print(" ---", end="")
    print("\n")

def checkWinner(board):
    for i in range(1, 3):
        r1 = board[0][0] == i and board[0][1] == i and board[0][2] == i
        r2 = board[1][0] == i and board[1][1] == i and board[1][2] == i
        r3 = board[2][0] == i and board[2][1] == i and board[2][2] == i
        c1 = board[0][0] == i and board[1][0] == i and board[2][0] == i
        c2 = board[0][1] == i and board[1][1] == i and board[2][1] == i
        c3 = board[0][2] == i and board[1][2] == i and board[2][2] == i
        d1 = board[0][0] == i and board[1][1] == i and board[2][2] == i
        d2 = board[0][2] == i and board[1][1] == i and board[2][0] == i
        if r1 or r2 or r3 or c1 or c2 or c3 or d1 or d2:
            print(f"Player {i} wins!")
            return True
        else: return False

board = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(9):
    while True:
        tile = input(f"Player {(i % 2) + 1}, please input a tile in the form of x,y\n")
        x, y = int(tile[0]), int(tile[-1])
        if board[x - 1][y - 1] is 0:
            board[x - 1][y - 1] = (i % 2) + 1
            break
        else:
            print(f"Tile {tile} is already taken. Please try again.\n")
    printBoard(board)
    if checkWinner(board):
        break