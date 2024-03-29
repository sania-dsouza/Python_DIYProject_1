# Program to place the input of the user onto the game board (list of lists)

import whoWonTTT as WWTT
# Assumptions
# Player 1: 'x'
# Player 2: 'o'
# Chances alternate between player 1 and 2

# Function that places the x's and o's in position on the row
def rowPlacerDef(gameRes, row, col, char):
    # This function checks if the row, col on the board is valid for placement
    while gameRes[row][col] != "-":
        print("{0} can't be placed here because the position is already taken.".format(char))
        # This chance must not be counted and the user must be given another chance if the position 
        # entered was not valid
        # Allow the user another shot
        row, col = map(int, input("Try again:").strip().split(','))
    
    gameRes[row][col] = char
        
    return gameRes

def printBlock(gameRes):
    for i in gameRes:
        print(i)

def fillLastSpace(gameRes, char):
    # fill up last character if one character is missing from the board
    ind = -1
    for k in range(3):
        if("-" in gameRes[k]):
            ind = gameRes[k].index("-")
            break
        else:
            continue
    return rowPlacerDef(gameRes, k, ind, char)

def getWinner(gameRes):
    winner = 0
    if gameRes[0].count("-")+gameRes[1].count("-")+gameRes[2].count("-") <= 4:
        winner = WWTT.findGameResult(gameRes)
    return winner
            
    
########################################################################################################
 
def placeUserInput():
    gameRes = [[], [], []]        # initialise the list of lists
    gameRes[0] = ['-', '-', '-']  # initialise the starting list which is going to be replaced everywhere on the list of lists
    gameRes[1] = ['-', '-', '-']
    gameRes[2] = ['-', '-', '-']

    while (gameRes[0].count("-")+gameRes[1].count("-")+gameRes[2].count("-")) > 0:

        # for player 1
        char = 'x'
        row, col = map(int, input("Where must your 'x' go? Enter in format row,col:").strip().split(','))
        gameRes = rowPlacerDef(gameRes, row, col, char)
        printBlock(gameRes)
        # code to check for a winner after the 5th user input has been taken
        if gameRes[0].count("-")+gameRes[1].count("-")+gameRes[2].count("-") <= 4:
            winner = getWinner(gameRes)
            if winner:
                print("The winner of this game of Tic Tac Toe is {0}".format(winner))
                print("This game ends here!")
                break
            else:
                if gameRes[0].count("-")+gameRes[1].count("-")+gameRes[2].count("-") == 0:
                    print("This game has no winner.")
                    print("This game ends here!")
                    break              
        
        # fill empty space
        if(gameRes[0].count("-")+gameRes[1].count("-")+gameRes[2].count("-")) == 1:
            print()
            print("Final board:")
            gameRes = fillLastSpace(gameRes, char='o')
            printBlock(gameRes)

            winner = getWinner(gameRes)
            if winner:
                print("The winner of this game of Tic Tac Toe is {0}".format(winner))
                print("This game ends here!")
                break
            else:
                print("This game has no winner.")
                print("This game ends here!")
                break 

        # for player 2
        char = 'o'
        row, col = map(int, input("Where must your 'o' go? Enter in format row,col:").strip().split(','))
        gameRes = rowPlacerDef(gameRes, row, col, char)
        printBlock(gameRes)
        # code to check for a winner after the 5th user input has been taken
        if gameRes[0].count("-")+gameRes[1].count("-")+gameRes[2].count("-") <= 4:
            winner = getWinner(gameRes)
            if winner:
                print("The winner of this game of Tic Tac Toe is {0}".format(winner))
                print("This game ends here!")
                break
            else:
                if gameRes[0].count("-")+gameRes[1].count("-")+gameRes[2].count("-") == 0:
                    print("This game has no winner.")
                    print("This game ends here!")
                    break    

        # fill empty space
        if(gameRes[0].count("-")+gameRes[1].count("-")+gameRes[2].count("-")) == 1:
            print()
            print("Final board:")
            gameRes = fillLastSpace(gameRes, char='x')
            printBlock(gameRes)
            
            winner = getWinner(gameRes)
            if winner:
                print("The winner of this game of Tic Tac Toe is {0}".format(winner))
                print("This game ends here!")
                break
            else:
                print("This game has no winner.")
                print("This game ends here!")
                break 



if __name__ == "__main__":
    placeUserInput()

    

