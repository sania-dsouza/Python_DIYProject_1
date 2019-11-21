# find the file overlap numbers between two files, one of which has prime numbers and another has happy numbers

with open('file1prime.txt', 'r') as open_file:
    file1 = open_file.read()
    file1Str = file1.split(", ")
    file1Int = [int(i) for i in file1Str]
    #print(file1Int)

with open('file2happy.txt', 'r') as open_file:
    file2 = open_file.read()
    file2Str = file2.split(", ")
    file2Int = [int(i) for i in file2Str]
    #print(file2Int)

file3 = []
for i in file1Int:
    if i in file2Int:
        file3.append(i)

print([i for i in file3])