list1 = []
list2 = []

with open("12_1.txt") as f:
    for line in f.readlines():
        a,b = line.split("   ")
        list1.append(int(a))
        list2.append(int(b))

list2NumberMap = {}
for num in list2:
    if num in list2NumberMap:
        list2NumberMap[num] += 1
        continue
    list2NumberMap[num] = 1

similarity = 0
for num in list1:
    if num not in list2NumberMap:
        continue
    similarity += num * list2NumberMap[num]

print(similarity)