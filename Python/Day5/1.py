import asyncio

rules = []
page_lists = []

with open("1.txt") as f:
    rulesText, pageListText = f.read().split("\n\n")
    for line in rulesText.split("\n"):
        rule = line.split("|")
        rules.append((int(rule[0]), int(rule[1])))
    
    for line in pageListText.split("\n"):
        pages = line.split(",")
        page_lists.append([int(page) for page in pages])

def middle_page(page_list):
    for i in range(len(rules)):
        flag = False
        for rule in rules:
            foundLast = False
            lastIndex = 0
            foundFirst = False
            firstIndex = 0
            for j, page in enumerate(page_list):
                if page == rule[1]:
                    foundLast = True
                    lastIndex = j
                if page == rule[0]:
                    foundFirst = True
                    firstIndex = j
            if foundLast and foundFirst and lastIndex < firstIndex:
                page_list[firstIndex], page_list[lastIndex] = page_list[lastIndex], page_list[firstIndex]
                flag = True
                continue
        if not flag and i == 0:
            return 0
    return page_list[int((len(page_list)-1)/2)]


middle_page_sum = 0
async def run(i, page_list):
    global middle_page_sum
    m = middle_page(page_list)
    print(i)
    middle_page_sum += m

async def main():
    tasks = [run(i, page_list) for i, page_list in enumerate(page_lists)]
    await asyncio.gather(*tasks)
    print(middle_page_sum)

asyncio.run(main())
