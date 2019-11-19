# Program to generate a fibonacci series

#get the number of fibonacci numbers that must be generated
def generateFibos(num):
    num1 = 0
    num2 = 1
    print(num1, num2, end=" ")
    for i in range(num-2):
        sum1 = num1+num2
        print(sum1, end = " ")
        num1 = num2
        num2 = sum1
    print()
        
num = int(input("How many Fibos must I generate?:"))

if num == 0:
    print("That is not a valid input")
elif num == 1:
    print("0")
elif num == 2:
    print("0 1")
else:
    #call the function to output the Fibos as required
    generateFibos(num)