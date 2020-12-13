import json
import re
with open('puzzle.json') as json_file:
    data = json.load(json_file)

def test_byr(field):
    if len(field) != 4:
        return False
    if int(field) < 1920 or int(field) > 2002:
        return False
    return True

def test_iyr(field):
    if len(field) != 4:
        return False
    if int(field) < 2010 or int(field) > 2020:
        return False
    return True

def test_eyr(field):
    if len(field) != 4:
        return False
    if int(field) < 2020 or int(field) > 2030:
        return False
    return True

def test_hgt(field):
    cm = re.search('[0-9]{3}cm', field)
    if cm:
        x = field.replace("cm", '')
        if int(x) < 150 or int(x) > 193:
            return False
        else:
            return True
    inch = re.search('[0-9]{2}in', field)
    if inch:
        x = field.replace("in", '')
        if int(x) < 59 or int(x) > 76:
            return False
        else:
            return True
    return False

def test_hcl(field):
    m = re.search('#[0-9a-f]{6}', field)
    if m:
        return True
    else:
        return False

def test_ecl(field):
    valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if field in valid_ecl:
        return True
    else:
        return False

def test_pid(field):
    m = re.search('[0-9]{9}', field)
    if m:
        return True
    else:
        return False


test_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0
valid_dicts = []
not_valid_dicts = []
for d in data:
    not_valid = 0
    for f in test_fields:
        if not_valid == 1:
            break
        if f in d.keys():
            continue
        else:
            not_valid = 1
    if not_valid == 1:
        continue
    if test_byr(d["byr"]) == False:
        not_valid = 1
        continue
    if test_iyr(d["iyr"]) == False:
        not_valid = 1
        continue
    if test_eyr(d["eyr"]) == False:
        not_valid = 1
        continue
    if test_hgt(d["hgt"]) == False:
        not_valid = 1
        continue
    if test_hcl(d["hcl"]) == False:
        not_valid = 1
        continue 
    if test_ecl(d["ecl"]) == False:
        not_valid = 1
        continue
    if test_pid(d["pid"]) == False:
        not_valid = 1
        continue
    if not_valid == 0:
        valid+=1
        valid_dicts.append(d)
print(f"Valid Passports: {valid}")
# print("---Valid Dicts---")
# print(valid_dicts)
# print("---Not Valid Dicts---")
# print(not_valid_dicts)