#!/usr/bin/python

'''
input data:
11
74 185 169
53 233 50
393 282 111
54 195 56
38 22 68
92 10 153
337 227 98
79 152 24
364 28 29
345 149 128
43 198 52
'''

subsetCount = int(input("Enter Number of Subsets: "))
numLists = list()
for _ in range(0, subsetCount):
    numLists.append(list(map(int, input("Enter 3 Numbers to Evaluate: ").split())))

for numList in numLists:
    numSum = int()
    numSum = numList[0] * numList[1] + numList[2]
    digitList = [int(digit) for digit in str(numSum)]
 
    digitSum = int()
    for digit in digitList:
        digitSum += digit
    print(digitSum)