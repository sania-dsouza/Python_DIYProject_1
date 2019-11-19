#Remove the duplicates of a list using two methods

# Method 1: Convert list to set
listA = [2,2, 3, 4,5, 4, 5, 6, 100, 100, 0.2  ]
setA = set(listA)
listA = list(setA)
print("Using sets:", listA)

# Method 2: Using lists
listB = []
for i in listA:
    if i not in listB:listB.append(i)
    else: continue
print("Using lists:", sorted(listB))