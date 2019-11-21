# Display the TicTacToe game board

# get the size of the game board from the user

size = int(input("What size board must it be? "))
#vertSiz = size+1   #For the vertical pipe
shape1 = "--- "*size
shape2 = "|   "*(size+1)
for i in range(size):
    print(" ", end="")
    print(shape1)
    print(shape2)
print(" ", end="")
print(shape1)
