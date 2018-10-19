strInput = str(input("Enter String: "))
listChars = list()
for char in strInput:
    listChars.append(char)
listReversedChars = listChars[::-1]
if listChars == listReversedChars:
    print("True")
else:
    print("False")