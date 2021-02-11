import random

number = random.randint(0,10)

print("Hey, yo. Guess a number")
userGuess = int(input())

while userGuess != number:
    if (userGuess) > number:
        print('too high. Try again.')
        userGuess = int(input())
    elif (userGuess) < number:
        print('too low. Try again.')
        userGuess = int(input())
print('Congrats! You did it!')