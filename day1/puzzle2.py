#Same data set as puzzle1
import json

with open('puzzle1.json') as json_file:
    data = json.load(json_file)

data.sort()
r = -1
while len(data) > 3:
    f = data.pop(0)
    x = 0
    y = 1
    
    while y < len(data):
        if f+data[x]+data[y] == 2020:
            r = f*data[x]*data[y]
            print(f"F: {f}, S: {data[x]}, T: {data[y]}, R: {r}")
            break
        if f+data[x]+data[y] > 2020:
            break
        x+=1
        y+=1
    if r != -1:
        break 

    

