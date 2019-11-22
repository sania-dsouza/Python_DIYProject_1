# Program to place the input of the user onto the game board (list of lists)

# Assumptions
# Player 1: x
# Player 2: o
# Chances alternate between player 1 and 2

# Function that places the x's and o's in position on the row
def rowPlacerDef(gameRes, row, col, char):
    # This function checks if the row, col on the board is valid for placement
    if gameRes[row][col] != "-":
        print("{0} can't be placed here because the position is already taken.".format(char))
    else:
        gameRes[row][col] = char
        
    return gameRes

########################################################################################################
 
gameRes = [[], [], []]    # initialise the list of lists
gameRes[0] = ['-', '-', '-']  # initialise the starting list which is going to be replaced everywhere on the list of lists
gameRes[1] = ['-', '-', '-']
gameRes[2] = ['-', '-', '-']

for i in range(4): # 9 is the total places to be filled, 4 chances per player to fill the board

    # for player 1
    char = 'x'
    row, col = map(int, input("Where must your 'x' go? Enter in format row,col:").strip().split(','))
    gameRes = rowPlacerDef(gameRes, row, col, char)
    print(gameRes)
    
    # for player 2
    char = 'o'
    row, col = map(int, input("Where must your 'o' go? Enter in format row,col:").strip().split(','))
    gameRes = rowPlacerDef(gameRes, row, col, char)
    print(gameRes)

#print([i for i in gameRes])