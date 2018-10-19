lstWords = list(map(str, input().split()))

lstRepeated = []
for word in lstWords:
    if lstWords.count(word) > 1 and word not in lstRepeated:
        lstRepeated.append(word)
lstRepeated.sort()
print(' '.join(map(str, lstRepeated)))

'''
input data:
nun lam mip tex bal pif sot bal bod tex end

answer:
bal tex
'''