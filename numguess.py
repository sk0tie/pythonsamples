import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1,20)
print(myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.')
    guess = int(input())
    
    guessesTaken += 1

    if guess < number:
        print('Higher.')
    if guess > number:
        print('Lower.')
    if guess == number:
        break
if guess == number:
    print('Peachy, ' + myName + '! You guessed my number in ' + str(guessesTaken) + ' tries!')

if guess != number:
    print('Piss off! The number I was thinking of was ' + str(number) + '.')