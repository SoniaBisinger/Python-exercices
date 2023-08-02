import random, os, time

def character1():
    player1 = input("\nName Your Legend: \n")
    breed = input("\nCharacter Type (Human, Elf, Wizard, Orc): \n")
    print()
    return player1

def character2():
    player2 = input("\nName Your Legend: \n")
    breed = input("\nCharacter Type (Human, Elf, Wizard, Orc): \n")
    print()
    return player2

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

def __health_check():
    if first_char_health > 0 and second_char_health > 0:
        print("\nAnd they're both standing for the next round!")
    elif first_char_health > 0 and second_char_health == 0:
        print(f"Oh no {player2} has died!")
        print(f"{player1} destroyed {player2} in {round} rounds!")
    else:
        print(f"\nOh no {player1} has died!")
        print(f"\n{player2} destroyed {player1} in {round} rounds!")

def __winner():
    if round == 1:
        print("\nThe battle begins!\n")
        print(winner + " wins the first blow ")
        print(loser + f" takes a hit with {damages} damage")
    else:
        print("\nThe battle continues!\n")
        print(winner + f" wins round {round}")
        print(loser + f" takes a hit with {damages} damage")


os.system("clear")
time.sleep(2)

print("⚔️ Battle Time ⚔️")

player1 = character1()
print(player1)

first_char_health = int(char_health(roll_6_sided_dice(), roll_12_sided_dice()))
print("HEALTH: " + str(first_char_health))

first_char_strenght = int(char_stats(roll_6_sided_dice(), roll_12_sided_dice()))
print("STRENGTH: " + str(first_char_strenght))

print("\nWho are the battling?\n")

player2 = character2()
print(player2)

second_char_health = int(char_health(roll_6_sided_dice(), roll_12_sided_dice()))
print("HEALTH: " + str(second_char_health))

second_char_str = int(char_stats(roll_6_sided_dice(), roll_12_sided_dice()))
print("STRENGHT: " + str(second_char_str))

time.sleep(2)
os.system("clear")
damages = abs(first_char_strenght - second_char_str)+1
round = 1
while True:
    os.system("clear")
    player1_roll = roll_6_sided_dice()
    player2_roll = roll_6_sided_dice()
    #player2 take damages for str difference + 1

    if first_char_health > 0 and second_char_health > 0:
        print("\n⚔️ Battle Time ⚔️\n")

        if player1_roll > player2_roll:
            winner = player1
            loser = player2

            __winner()

            print("\n" + player1)
            print("HEALTH: " + str(first_char_health))

            second_char_health -= damages
            print("\n" + player2)
            print("HEALTH: " + str(second_char_health))

            __health_check()

            round += 1
            time.sleep(8)
            os.system("clear")
            continue
        else:
            winner = player2
            loser = player1
            __winner()

            first_char_health -= damages
            print("\n" + player1)
            print("HEALTH: " + str(first_char_health))

            print("\n" + player2)
            print("HEALTH: " + str(second_char_health))

            __health_check()

            round += 1
            time.sleep(8)
            os.system("clear")
            continue
    else:
        break
