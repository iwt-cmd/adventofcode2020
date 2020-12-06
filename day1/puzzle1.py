import json

with open('puzzle1.json') as json_file:
    data = json.load(json_file)

data.sort()

x = len(data)
while x > 0:
    f = data.pop(0)
    r = 0
    for d in data:
        if f + d == 2020:
            r = f*d
            print(f"F: {f}, D: {d}, R: {r}")
            break
        if f + d > 2020:
            break
    if r != 0:
        break
    else:
        x -= 1
    

