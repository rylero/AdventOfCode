list1 = []
list2 = []

with open("12_1_1.txt") as f:
    for line in f.readlines():
        a,b = line.split("   ")
        list1.append(int(a))
        list2.append(int(b))

list1.sort()
list2.sort()

sum = 0
for a,b in zip(list1, list2):
    sum += abs(a - b)

print(sum)