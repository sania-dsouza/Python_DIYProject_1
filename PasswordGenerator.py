#This program will generate a password for you according to the rules you specify
#the only pre-existing rule is that the password has to be atleast 6 characters long

# Determine the length of the password
while(1):
    try:
        passL = input("Enter the length of the desired password in the format 'minL-maxL':")
    except Exception as e:
        print("Retry please. Follow the format for the password length specification.")
    else:
        break
    finally:
        pass

# Determine if the password must include special characters, numbers and upper-case, lower-case characters (separately)
passChar = input("Can the password have special characters? (y/n): ")
passNum = input("Can the password have numbers? (y/n): ")
passUpLoMix = input("Can the password have a mix of upper and lower characters? (y/n): ")
if!(passUpLoMix): 
    passLo = input("Lower-case characters? (y/n): ")

passwordGen(passL, passChar, passNum, passUpLoMix, passLo)

# General password rules this program follows:
# The password that is generated has a minimum of 2 numbers, 2 upper-case letters, 
# two special characters and the rest are lower-case characters
def passwordGen(passL, passChar, passNum, passUpLoMix, passLo):    
    




