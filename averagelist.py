subsetCount = int(input("Enter Number of Subsets: "))
numLists = list()
for _ in range(0, subsetCount):
    numLists.append(list(map(int, input("Enter Numbers to Average: ").split())))

def avg(numList):
    sum = int()
    for num in numList:
        sum += num
    return round(sum / (len(numList) - 1))

for numList in numLists:
    print(avg(numList))