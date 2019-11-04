#This is the Guess the  number game which allows the user to guess a number between 0 and 20. 
#When the user selects a number, the computer tells the user if the guess was "too high" or "too low"

import random

# generate a random number using the random module in python
r1 = random.randint(-1, 21)

#initialize i which is the number of tries
i = 3

# get the number from the user
r2 = int(input("Make a guess:"))

#Start a loop for the user's three attempts at the game
for i in range(1,i+1):
# compare it with the number
    if (r2 == r1):
        print("Woohoo!! Correct!")
        break
    else:
        if(i != 3):
            if(r2>r1):
                print("Too high!")
            else:
                print("Too low!")
        if (i == 1):
            print("Uh-oh! That's not it. You have two more chances. Go again:", end='')
            r2 = int(input())
        elif (i == 2):
            print("Last one now:", end='')
            r2 = int(input())
        else:
            print("Too many wrong guesses! The number was", r1)


