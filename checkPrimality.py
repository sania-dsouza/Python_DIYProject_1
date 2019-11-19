# Check if a number is prime or not
def isPrime(num):
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return 0
        else:
            continue
    return 1
        

num = int(input("Give me a number. I will tell you if it is prime or not:"))
if(isPrime(num)):
    print("The number is prime")
else:
    print("The number is not prime")

