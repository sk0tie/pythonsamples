subset = int(input("Enter Subset: "))
numLists = list()
for _ in range(0, subset):
    numLists.append(list(map(int, input("Enter Pair: ").split())))
for numList in numLists:
    if numList[0] <= numList[1]:
        print(numList[0])
    else:
        print(numList[1])