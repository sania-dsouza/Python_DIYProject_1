#This is the Guess the  number game which allows the user to guess a number between 0 and 20. 
#When the user selects a number, the computer tells the user if the guess was "too high" or "too low"

import random
def isInputInvalid(r2):
    if(r2>20 or 0>r2):
        return True
    else:
        return False

# generate a random number using the random module in python
r1 = random.randint(0, 20)  # randint treats the arguments as inclusive
i = 10

#Start a loop for the user's three attempts at the game
for it in range(0,i):  #it = iterator
    r2 = int(input("Make a guess: "))
    if(isInputInvalid(r2)): 
        if(it==(i-1)): print("Too many wrong guesses! The number was", r1)
        else: 
            print("Your input must be between 0 and 20, both inclusive")
            continue
    else:
        if (r2 == r1):
            print("Woohoo!! Correct!")
            break
        else:
            if(it>=0 and it<(i-1)):
                if(r2>r1):
                    print("Too high!")
                else:
                    print("Too low!")
                print("You have", (i-it-1) , "more chances. ", end='')
            else:
                print("Too many wrong guesses! The number was", r1)
        

        