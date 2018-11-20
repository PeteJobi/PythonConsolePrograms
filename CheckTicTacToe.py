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
            break

print(checkWinner([[1,2,0],[2,1,0],[2,1,1]]))