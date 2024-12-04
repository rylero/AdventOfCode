import re

txt = ""
with open("data.txt") as f:
    txt = f.read()

instructions = re.findall("(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", txt)

enabled = True
sum = 0
for command in instructions:
    if command[1]: # do
        enabled = True
    elif command[2]: # dont
        enabled = False
    elif command[0] and enabled: # mul
        numbers = [int(x) for x in command[0].replace("mul(", "").replace(")", "").split(",")]
        sum += numbers[0] * numbers[1]

print(sum)