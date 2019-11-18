# Program that simulates the Hangman between the user and the computer
import random 

# Initialise word list for game
wordList = ["desk", "bed", "table", "chair", "cupboard"]

# Let computer pick up random word out of the list
word = random.choice(wordList)
wordDisplay = "_ "*len(word)
chances = len(word) # logic to get the number of chances available to the user  

print("Let's play Hangman!")
print("*******************")
print()
print("The computer has chosen a word. Now, let's start")
print(wordDisplay)
print("What's your first letter?")

while chances > 0:
    l = input()
    if(l not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
        l = print("Non-literal characters are not allowed! Try again.")
    elif(len(l) > 1):
        l = print("One letter at a time is only allowed. Try again")
    else:
        # the letter entered is present in the word
        if l in str(word):
            for i in range(0,len(word)):
                if(l == word[i]):
                    lst = list(wordDisplay)
                    lst[i*2] = l
                    wordDisplay = "".join(lst)
            print("Right!")
            print(wordDisplay)   
        else:
            # the letter entered is not present in the word
            print("That's not right.")
            if(chances > 1):
                print(wordDisplay)
                print("Go again:")
    chances-=1
    
if word == wordDisplay.replace(" ", ""):
    print("You got the word right!")
else:
    print("That was your last chance! The word was", word)
            

    

        


        
        

