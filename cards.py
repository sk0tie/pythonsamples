lstSuit = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
lstRank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

intNumCards = int(input())
lstCards = list(map(int, input().split()))

for card in lstCards:
    suit = round((card // 13), 0)
    rank = card % 13
    print(lstRank[rank] + '-of-' + lstSuit[suit], end=' ')

'''
example
input data:
26
22 12 29 17 10 5 42 45 48 47 8 18 28 14 15 16 44 27 30 7 23 13 11 46 31 51

answer:
Ace-of-Spades 8-of-Diamonds Ace-of-Hearts 9-of-Spades 8-of-Clubs
'''