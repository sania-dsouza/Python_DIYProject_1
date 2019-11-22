# Program to place the input of the user onto the game board (list of lists)

# Assumptions
# Player 1: x
# Player 2: o
# Chances alternate between player 1 and 2


# Changes to be made:
#1 Make the input requesting end when the number empty blocks goes to 1
#2 Auto-fill the last character
#3 display the board in board format after each placement
#4 connected with #1 and #2: repeat a character input and placement if the previous try was invalid

# Function that places the x's and o's in position on the row
def rowPlacerDef(gameRes, row, col, char):
    # This function checks if the row, col on the board is valid for placement
    if gameRes[row][col] != "-":
        print("{0} can't be placed here because the position is already taken.".format(char))
        # This chance must not be counted and the user must be given another chance if the position 
        # entered was not valid
    else:
        gameRes[row][col] = char
        
    return gameRes

########################################################################################################
 
gameRes = [[], [], []]    # initialise the list of lists
gameRes[0] = ['-', '-', '-']  # initialise the starting list which is going to be replaced everywhere on the list of lists
gameRes[1] = ['-', '-', '-']
gameRes[2] = ['-', '-', '-']

while (gameRes[0].count("-")+gameRes[1].count("-")+gameRes[2].count("-")) > 0:

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

    #print(gameRes[0].count("-")+gameRes[1].count("-")+gameRes[2].count("-"))

for i in gameRes:
    print(i)