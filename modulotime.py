'''
input data:
3
1 0 0 0 2 3 4 5
5 3 23 22 24 4 20 45
8 4 6 47 9 11 51 13

answer:
(1 3 4 5) (19 0 57 23) (1 7 44 26)
'''

subsetCount = int(input("Enter Number of Subsets: "))
numLists = list()
for _ in range(0, subsetCount):
    numLists.append(list(map(int, input("Enter Date String: ").split())))

for numList in numLists:
    day1,hour1,min1,sec1 = numList[0:4]
    day2,hour2,min2,sec2 = numList[4:8] 

    startDateSecs = (day1 * 86400) + (hour1 * 3600) + (min1 * 60) + (sec1)
    endDateSecs = (day2 * 86400) + (hour2 * 3600) + (min2 * 60) + (sec2)

    differenceSecs = (endDateSecs - startDateSecs)

    minutes, seconds = divmod(differenceSecs, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    print('(' + str(days), str(hours), str(minutes), str(seconds) + ')', end = " ")
    