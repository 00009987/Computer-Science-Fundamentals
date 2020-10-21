def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)


userInput = int(input('Enter a number: '))

if userInput > 0:
    countdown(userInput)
elif userInput < 0:
    countup(userInput)
else:
    print('Blastoff!')

