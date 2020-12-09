def slope(horz, vert, d):
    h = 0
    v = 0
    t = 0
    f = 1
    while v < len(d):
        x = d[v].rstrip()
        l = len(x)
        if h >= len(x):
            f+=1
        x = x*f
        if x[h] == "#":
            t+=1
        v+=vert
        h+=horz
    return t

with open("/home/jbanfield/projects/aoc/adventofcode2020/day3/puzzle.txt", "r") as map:
    data = map.readlines()

s1 = slope(1,1, data)
s2 = slope(3,1, data)
s3 = slope(5,1, data)
s4 = slope(7,1, data)
s5 = slope(1,2, data)
print(f"S1: {s1}, S2: {s2}, S3: {s3}, S4: {s4}, S5: {s5}")
final = s1*s2*s3*s4*s5
print(f"Final: {final}")
