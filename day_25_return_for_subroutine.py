import random
print("Character stat generator")
#1. rolls a dice of any size and return number
def roll_infinite_sided_dice():
    number1 = random.randrange(100)
    return number1

#2. roll one six-sided dice
def roll_six_sided_dice():
    number2 = random.randint(1, 6)
    return number2

#3. roll one eight-sided dice
def roll_eight_sided_dice():
    number3 = random.randint(1, 8)
    return number3

#4. multiply number2 * number3
def multiplication(number2, number3):
    health = str(number2 * number3)
    return health + "hp"
while True:

    name = input("Name your warrior: " + "\033[1;32m")
    if name != "":
        print("\033[0;37m" + "Their health is: " + multiplication(roll_six_sided_dice(), roll_eight_sided_dice()))
        continue
    else:
        print("\033[0;31m" + "Game ended")
        break
