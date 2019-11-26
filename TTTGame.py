#The final game board

import TTTGameBoard, TTTGamePlacer, whoWonTTT

print()
print("Welcome to the world's favorite game: TIC TAC TOEEEE!!")
print("******************************************************")
print()
print("Let's start with a 2-player 3x3 board")
print()

#Outputs the game board
TTTGameBoard.displayGameBoard()

#Gets the user input and saves it in a variable
TTTGamePlacer.placeUserInput()

