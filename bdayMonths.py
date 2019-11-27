# get the number of people born in the same month

import calendar
import bdayJson
from collections import Counter

#get the month from the dates in the json file
bJson = bdayJson.readJson()
arr = []   #get the dates in a list
for key in bJson.keys():
    arr.append(bJson[key])

# get the months from the list 'arr'
arr = list(map(int, [i.split('-')[1] for i in arr]))  
arr1 = []

#get the month name here using Calendar
for i in arr:
    arr1.append([k for v,k in enumerate(calendar.month_name)][i])
#print(arr1)

# apply the 'Counter' to get the count of the number of repeated months
d = dict(Counter(arr1))     # this returns a dictionary with the month number and the count of each

print(d)