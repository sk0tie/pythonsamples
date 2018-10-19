subset = int(input("Enter Subset: "))
numLists = list()
for _ in range(0, subset):
    numLists.append(list(map(int, input("Enter Pair: ").split())))
for numList in numLists:
    sum = numList[0] + numList[1]
    print(sum)