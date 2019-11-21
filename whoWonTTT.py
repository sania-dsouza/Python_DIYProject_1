import ticTacToeGameboard as ttt_Board
def doWeHaveAWinner(gameRes):
    winner = 0
    # Check the row results for a winner
    for i in range(3):
        if gameRes[i][0] == gameRes[i][1] == gameRes[i][2]:
            winner = gameRes[i][0]
            break
        else:
            continue
    
    # Check the column results for a winner
    for j in range(3):
        if gameRes[0][j] == gameRes[1][j] == gameRes[2][j]:
            winner = gameRes[0][j]
            break
        else:
            continue

    # Check the diagonals for a winner
    if gameRes[0][0] == gameRes[1][1] == gameRes[2][2]:
        winner = gameRes[1][1]
    elif gameRes[0][2] == gameRes[1][1] == gameRes[2][0]:
        winner = gameRes[1][1]
    
    return winner

print("The Tic-Tac-Toe game board is:",ttt_Board.size)

gameRes = [[], [], []]
gameRes[0] = list(map(int, input("What is the first row of entries:").strip().split()))
gameRes[1] = list(map(int, input("What is the second row of entries:").strip().split()))
gameRes[2] = list(map(int, input("What is the third row of entries:").strip().split()))

# Look for a winner
win = doWeHaveAWinner(gameRes)
if(win == 0):
    print("There was no winner!")
else:
    print("Player {0} won!".format(win))
    




