# Program to reverse string words 

wordString = input("Input a string:")

print("The reversed string is:", end = " ")

wordString = wordString.split()
print(" ".join(wordString[::-1]))