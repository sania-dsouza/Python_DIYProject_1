# Give me the list of divisors of a number

num = int(input("Enter a number:"))

for i in range(1, int(num/2)+1):
    if num%i == 0:
        print(i)
print(num)
