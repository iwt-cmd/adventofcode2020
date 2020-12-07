#For purposed of this exercise, "min" and "max" will be used as the 2 postion numbers to avoid created a new json file or having to modify puzzle1.py

import json

with open("puzzle.json") as json_file:
    data = json.load(json_file)

valid_pw = 0

for d in data:
    pw = d['password']
    f = int(d['min'])-1
    s = int(d['max'])-1
    letter1 = pw[f]
    letter2 = pw[s]
    if letter1 == letter2:
        continue
    if letter1 == d['letter'] or letter2 == d['letter']:
        valid_pw+=1

print(f"Valid Passwords: {valid_pw}")