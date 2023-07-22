import random
print("Infinity Dice 🎲")

def roll_dice(sides):
    number = random.randint(1, sides)
    print("You rolled", number)

sides = int(input("How many sides?: "))

roll_dice(sides)

while True:
    playAgain = input("Roll again? ")
    if playAgain == "yes":
        roll_dice(sides)
        continue
    elif playAgain == "no":
        break
    else:
        print("Wrong answer, you may say yes or no")
        continue
