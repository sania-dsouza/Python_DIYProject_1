# Birthdays returned from a JSON file

import birthdayDictionaries as disBday
import json

def readJson():
    with open("bdayJson.json", "r") as f:
        dictBday = json.load(f)
    return dictBday

#print(dictBday)
#disBday.displayBday(dictBday)

if __name__ == "__name__":
    readJson()


