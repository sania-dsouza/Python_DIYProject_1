# Play the Cows and Bulls game with the computer

import random

num = random.randint(1000, 9999)
chances = 10
print("Let's play COWS 'n' BULLS")
print("*************************")
print("The computer has chosen a number. Now it is your turn to guess. You have an infinite number of chances.")
print("Your first guess:")

while(chances > 0):
    guess = input()
    cows, bulls = 0, 0
    for i in range(4):
        if(str(guess)[i] in str(num)):
            if(str(guess)[i] == str(num)[i]):
                cows+=1
            else:
                bulls+=1
    if(cows != 4):
        print("You have {0} cows and {1} bulls".format(cows, bulls))
        print("The number was", num)
    else:
        print("You guessed it correctly!")
        break
    chances-=1



