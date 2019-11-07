#This is the Rock, Paper, Scissors game which allows the user to play the age-old game with the computer

import random
def attemptDecider(ca, ua, scores):
    cac,uac= 0,0
    if(ca!=ua):
        if(ca=="rock"):
            if(ua=="paper"):
                uac=1
            else:
                cac=1
        elif(ca=="paper"):
            if(ua=="rock"):
                cac=1
            else:
                uac=1
        else:
            if(ua=="rock"):
                uac=1
            else:
                cac=1
    scores[0]+=cac
    scores[1]+=uac
    return scores

choices = ["rock", "paper", "scissor"]
scores = [0,0]

for i in range(0,10):     #the user and computer play 10 times thru the game
    compatt = random.choice(choices)
    while(1):
        useratt = input("Choose one of rock, paper or scissor: ")
        if(useratt in choices):
            scores = attemptDecider(compatt, useratt, scores)
            print("The scores are:")
            print("Computer: ", scores[0])
            print("User: ", scores[1])
            break
        else:
            print("Please choose one of rock, paper or scissor. Note the plural-singular difference.")
            #Do not reduce the number of chances available to the user to play the game because of an invalid choice. 
            #Let her continue playing till she produces a valid input
            continue
    
print("The winner is", "the computer!" if scores[0] > scores[1] else "the user!")