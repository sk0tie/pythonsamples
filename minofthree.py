subset = int(input("Enter Subset: "))
numLists = list()
for _ in range(0, subset):
    numLists.append(list(map(int, input("Enter Triplet: ").split())))
for numList in numLists:
    if numList[0] <= numList[1] and numList[0] <= numList[2]:
        print(numList[0])
    elif numList[1] <= numList[0] and numList[1] <= numList[2]:
        print(numList[1])
    else:
        print(numList[2]) 