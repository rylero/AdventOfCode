grid = []
with open("1.txt") as f:
    grid = [list(line.replace("\n", "")) for line in f.readlines()]

count = 0

def cube(i, j):
    c = []
    for x in range(3):
        a = []
        for y in range(3):
            a.append(grid[i+x][j+y])
        c.append(a)
    return c

count = 0
for i in range(0, len(grid)-2):
    for j in range(0, len(grid[0])-2):
        c = cube(i, j)
        if c[1][1] != "A":
            continue
        if not ((c[0][0] == "M" and c[2][2] == "S") or (c[0][0] == "S" and c[2][2] == "M")):
            continue
        if not ((c[0][2] == "M" and c[2][0] == "S") or (c[0][2] == "S" and c[2][0] == "M")):
            continue
        count += 1

print(f"Found: {count}")