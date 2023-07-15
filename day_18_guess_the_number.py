import random

print("Welcome to guess-the-number game!")
print("It's simple : computer will generate a number between 0 and 100")
print("And you have to find this number :) Good Luck ! ")
print("........")
print("Let's starting")

numberToGuess = random.randrange(100)

tries = 0

while True:

    print("What's the number i guessed?: ")
    userGuess = int(input(""))

    if userGuess < numberToGuess :
        print("Too low! Try again")
        tries += 1
        continue
    elif userGuess > numberToGuess :
        print("Too high!")
        tries += 1
        continue
    else:
        print("Correct! You guessed the number ;) ")
        if tries > 1:
            print(f'And you did in in {tries} tries')
        else:
            print('And you did in in one stroke!')
        break

print("Game is over, see you")
