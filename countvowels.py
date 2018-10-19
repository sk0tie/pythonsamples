subsetCount = int(input())
stringList = []
for _ in range(0, subsetCount):
    stringList.append(str(input().lower()))

for string in stringList:
    vowels = int()
    for char in string:
        if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "y"):
            vowels += 1
    print(vowels)
