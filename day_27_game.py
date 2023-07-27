import random, os, time

print("Character Builder")

while True:

    def character():
        name = input("\nName Your Legend:\n")
        breed = input("\nCharacter Type (Human, Elf, Wizard, Orc): \n")
        print("\n" + name)

    def roll_6_sided_dice():
        return random.randint(1, 6)

    def roll_12_sided_dice():
        return random.randint(1, 8)

    def char_health(roll_6_sided_dice, roll_12_sided_dice):
        health = ((roll_6_sided_dice * roll_12_sided_dice)/2)+10
        return health

    def char_stats(roll_6_sided_dice, roll_12_sided_dice):
        health = ((roll_6_sided_dice * roll_12_sided_dice)/2)+12
        return int(health)

    os.system("clear")
    time.sleep(2)

    character()
    print("HEALTH: " + str(int(char_health(roll_6_sided_dice(), roll_12_sided_dice()))))
    print("STRENGTH: " + str(int(char_stats(roll_6_sided_dice(), roll_12_sided_dice()))))
    print("\nMay your name go down in Legend...\n")

    choice = input("Wanna play again?\n").upper()

    if choice == "YES":
        continue
    else:
        print("\nGame Over")
        break
