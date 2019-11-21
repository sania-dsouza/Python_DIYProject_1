# Program to place the input of the user onto the game board (list of lists)

# Assumptions
# Player 1: x
# Player 2: o
# Chances alternate between player 1 and 2

# Function that places the x's and o's in position on the row
def rowPlacerDef(col, char):
    





gameRes = [[], [], []] 
rowRes = ['-', '-', '-']

for i in range(4): # 9 is the total places to be filled

    # for player 1
    row, col = map(int, input("Where must your 'x' go? Enter in format row,col:").strip().split(','))
    rowRes = rowPlacerDef(col, 'x')
    gameRes[row] = rowRes
    print(gameRes)

    # for player 2
    row, col = map(int, input("Where must your 'o' go? Enter in format row,col:").strip().split(','))
    rowRes = rowPlacerDef(col, 'o')   
    gameRes[row] = rowRes
    print(gameRes)

print([i for i in gameRes])