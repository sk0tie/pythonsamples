subsetCount = int(input("Enter Subset Count: "))
numList = []
for _ in range(0, subsetCount):
    numList.append(int(input("Enter Number: ")))

for num in numList:
    if num == 0:
        print(0)
    if num == 1:
        print(3)
    listFibs = [0,1]
    lastIndex = 0
    currentIndex = 1
    for x in range(2,1001):
        y = listFibs[lastIndex] + listFibs[currentIndex]
        listFibs.append(y)
        lastIndex = currentIndex
        currentIndex += 1
        if (y == num):
            print(currentIndex)

