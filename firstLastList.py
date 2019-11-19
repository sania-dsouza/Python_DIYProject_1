# Program to output the first and last element of the list

listA = list(map(int, input("Enter the numbers:").strip().split()))
print([listA[i] for i in range(0, len(listA)) if(i == 0 or i == len(listA)1)])



