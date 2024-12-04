fileLines = []
with open("12_2.txt") as f:
    fileLines = f.readlines()

lines = []
for line in fileLines:
    lines.append([int(x) for x in line.split()])

print(len(lines))

count = 0
for i, fullLine in enumerate(lines):
    for j in range(len(fullLine)):
        linenodiff = []
        for k, a in enumerate(fullLine):
            if (k != j):
                linenodiff.append(a)
        line = []
        last = linenodiff[0]
        for num in linenodiff[1:]:
            line.append(num-last)
            last = num
        firstSign = -1
        if line[0] >= 1:
            firstSign = 1
        for num in line:
            if abs(num) < 1:
                break
            if abs(num) > 3:
                break
            if firstSign == -1 and num > 0:
                break
            if firstSign == 1 and num < 0:
                break
        else:
            print(line)
            count += 1
            break

print(f"Safe: {count}")