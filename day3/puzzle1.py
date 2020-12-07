with open("puzzle.txt", "r") as map:
    data = map.readlines()


h = 0
v = 0
t = 0
f = 1
while v < len(data):
    x = data[v].rstrip()
    if h > len(x):
        f+=1
    x = x*f
    if x[h] == "#":
        t+=1
    v+=1
    h+=3

print(f"Trees: {t}")