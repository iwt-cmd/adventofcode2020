import json

with open('puzzle.json') as json_file:
    data = json.load(json_file)

test_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid = 0
for d in data:
    not_valid = 0
    for f in test_fields:
        if not_valid == 1:
            break
        if f in d.keys():
            continue
        else:
            not_valid = 1  
    if not_valid == 0:
        valid+=1

print(f"Valid Passports: {valid}")