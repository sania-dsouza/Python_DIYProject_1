# Birthdays returned from a JSON file

import birthdayDictionaries as disBday
import json

with open("bdayJson.json", "r") as f:
    dictBday = json.load(f)

print(dictBday)
disBday.displayBday(dictBday)

