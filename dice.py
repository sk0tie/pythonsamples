intNumRolls = int(input())
listRolls = list()
for _ in range(0, intNumRolls):
    listRolls.append(float(input()))
for roll in listRolls:
    print(int((roll * 6 + 1)), end=' ')
'''
6
0.59558786964
0.861037873663
0.385597702116
0.246237673331
0.808033385314
0.0544673665427

answer:
4 6 3 2 5 1
'''