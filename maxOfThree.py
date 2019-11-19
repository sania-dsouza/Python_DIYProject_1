# Find the maximum of three numbers in a list without using max()

listA = list(map(int, input("Enter the list of three numbers:").strip().split()))

maxi = listA[0]

for i in [0,1,2]:
    if listA[i] > maxi:
        maxi = listA[i]

print("the largest of the three numbers is", maxi)
