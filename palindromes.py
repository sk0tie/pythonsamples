intNumPals = int(input())
lstPals = list()
lstIllegalChars = ['.', ',', '?', '!', '-', ' ']
for _ in range(0, intNumPals):
    lstPals.append(str(input()))
for pal in lstPals:
    lstPalChars = list()
    for char in pal:
        if char not in lstIllegalChars:
            lstPalChars.append(char.lower())
    if lstPalChars == lstPalChars[::-1]:
        print('Y', end=' ')
    else:
        print('N', end=' ')
