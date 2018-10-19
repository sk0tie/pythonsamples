subset = int(input("Enter Subset: "))
numLists = list()
for _ in range(0, subset):
    numLists.append(list(map(int, input("Enter Pair: ").split())))
for numList in numLists:
    print(round(numList[0] / numList[1]))