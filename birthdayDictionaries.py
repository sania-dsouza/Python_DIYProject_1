 # Program to return the birthday of a famous personality out of a list thaty is already prepared. 

nameDict = {} # main dict with the names and the birthdays.

# get the user input to fill the dictionary  (10 birthdays for now)
for i in range(2):
    name = str(input("Name of the personality:"))
    bday = str(input("Birthday with separator '-':"))
    nameDict[name] = bday
    #print(nameDict)
    #print(nameDict[name])

print("Know the birthday of a famous persoanlity:")
person = input("Name of the personality:")
print("The bday of {0} is on {1}".format(person, nameDict[person]))
