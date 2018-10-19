'''
input data:
3
9 15 1776

answer:
9 11 60
'''

subsetCount = int(input("Enter Subset Count: "))
numList = list(map(int, input("Enter Number String: ").split()))

def wsd(num):
    digitSum = int()
    digitList = [int(digit) for digit in str(num)]
    for position, digit in enumerate(digitList):
        digitSum += digit * (position + 1)
    return(digitSum)

for num in numList:
    print(wsd(num))