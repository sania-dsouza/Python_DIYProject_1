# Program to find whether a string is a palindrome or not

string = input("Input a string:")
string.strip()

revString = ''.join(reversed(string))

if(string == revString): 
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")