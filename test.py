for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

for i in range(1,101):
    result = ""
    if i % 3 == 0:
        result += 'fizz'
    if i % 5 == 0:
        result += 'buzz'
    if len(result) == 0:
        result = i
    print(result)

for i in range(1,101):
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

i = 101
if i % 15 == 0:
    print('fizzbuzz')
elif i % 3 == 0:
    print('fizz')
elif i % 5 == 0:
    print('buzz')
else:
    print(i)