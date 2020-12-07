import json

with open('puzzle.json') as json_file:
    data = json.load(json_file)

valid_pw = 0
for d in data:
    count = 0
    for l in d['password']:
        if l == d['letter']:
            count+=1
        if count > int(d['max']):
            break
    if count <= int(d['max']) and count >= int(d['min']):
        valid_pw+=1

print(f"Valid Passwords: {valid_pw}")