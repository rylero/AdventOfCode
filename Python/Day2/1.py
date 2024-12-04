fileLines = []
with open("12_2.txt") as f:
    fileLines = f.readlines()

lines = []
for line in fileLines:
    lines.append([int(x) for x in line.split()])

print(len(lines))

differences = []
for line in lines:
    lineDifference = []
    last = line[0]
    for num in line[1:]:
        lineDifference.append(num-last)
        last = num
    differences.append(lineDifference)

count = 0
for i, line in enumerate(differences):
    firstSign = -1
    if line[0] >= 1:
        firstSign = 1
    for num in line:
        if abs(num) < 1:
            print("FAIL", line, ":", lines[i])
            break
        if abs(num) > 3:
            print("FAIL", line, ":", lines[i])
            break
        if firstSign == -1 and num > 0:
            print("FAIL", line, ":", lines[i])
            break
        if firstSign == 1 and num < 0:
            print("FAIL", line, ":", lines[i])
            break
    else:
        print("SUCCESS", line, ":", lines[i])
        count += 1

print(f"Safe: {count}")