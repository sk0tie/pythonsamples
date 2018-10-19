numList = list(map(int, input("Enter Number String: ").split()))
for num in range(1, numList[0] + 1):
    print(round(((numList[num] + 40) / 1.8) - 40))
