# caesar chipher

MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Caesar Cipher')
        print('-------------')
        print('[E]ncrypt')
        print('[D]ecrypt')
        print('[B]rute')
        print()
        print('Command:', end=' ')

        mode = input().lower()
    
        if mode in 'encrypt e decrypt d brute b'.split():
            return mode
        else:
            print('Unknown command.')
            print()

def getMessage():
    print('Enter Message: ', end=' ')
    return input()

def getKey():
    key = int()
    while True:
        print('Enter Key:', end=' ')
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = str()

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            
            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()
    
print('Translated Message(s):')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(getTranslatedMessage('decrypt', message, key))
