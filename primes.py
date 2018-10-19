'''
listPrimes = list()
for possiblePrime in range(2, 200000):
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
            break
    if isPrime:
        listPrimes.append(possiblePrime)
print(listPrimes)
'''
   
# Initialize a list
primes = []
for possiblePrime in range(2, 200001):
    # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(possiblePrime)
print(primes[7])