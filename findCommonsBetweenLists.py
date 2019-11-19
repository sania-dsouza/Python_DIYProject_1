# Program to find the common numbers in two lists

listA = list(map(int, input("Enter the first list: ").strip().split()))
listB = list(map(int, input("Enter the second list: ").strip().split()))

print([i for i in listA if i in listB])  #list comprehension