subset = int(input("Enter Subset: "))
numList = list(map(int, input("Enter Number String: ").split()))
sum = int()
for num in range(0, subset):
    sum += numList[num]
print(sum)