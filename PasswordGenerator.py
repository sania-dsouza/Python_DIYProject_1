#This program will generate a password for you according to the rules you specify
#the only pre-existing rule is that the password has to be atleast 6 characters long

import random

# Determine the length of the password
while(1):
    try:
        passL = int(input("Enter the length of the desired password:"))
    except Exception as e:
        print("Retry please. Follow the format for the password length specification.")
    else:
        break
    finally:
        pass

# Determine if the password must include special characters, numbers and upper-case, lower-case characters (separately)
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passwd =  "".join(random.sample(s,passL))
print(passwd)







