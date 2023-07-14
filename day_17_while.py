from getpass import getpass as input
print("Welcome to paper, rock, scissors game!")

player1Score = 0
player2Score = 0
while player1Score < 2 or player2Score < 2:

    if player1Score == 3 or player2Score == 3:
        print("game finished")
        print(f'Player 1 score is {player1Score}, \n Player 2 score is {player2Score}')
        break

    # print(f'{player1Score}, {player2Score}')
    print("\nPlayer 1 choose your move: ")
    player1Move = input("")

    print("Player 2 choose your move: ")
    player2Move = input("")

    if player1Move=="R":

        if player2Move=="R":
            print("You both picked Rock, draw!")
            print(f"\nPlayer 1 score = {player1Score} \nPlayer 2 score = {player2Score}")

        elif player2Move=="S":
            player1Score += 1
            print("Player1 smashed Player2's Scissors into dust with their Rock!")
            print(f"\nPlayer 1 score = {player1Score} \nPlayer 2 score = {player2Score} \n")

        elif player2Move=="P":
            print("Player1's Rock is smothered by Player2's Paper!")
            player2Score += 1
            print(f"\nPlayer 1 score = {player1Score} \nPlayer 2 score = {player2Score} ")

        else:
            print("Invalid Move Player 2!")
        continue

    elif player1Move=="P":

        if player2Move=="R":
            print("Player2's Rock is smothered by Player1's Paper!")
            player1Score += 1
            print(f"\nPlayer 1 score = {player1Score} \nPlayer 2 score = {player2Score} \n")

        elif player2Move=="S":
            print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
            player2Score += 1
            print(f"\nPlayer 1 score = {player1Score} \nPlayer 2 score = {player2Score} \n")

        elif player2Move=="P":
            print("Two bits of paper flap at each other. Dissapointing. Draw.")
            print(f"\nPlayer 1 score = {player1Score} \nPlayer 2 score = {player2Score} \n")

        else:
            print("Invalid Move Player 2!")
        continue

    elif player1Move=="S":
        if player2Move=="R":
            print("Player 2's Rock makes metal-dust out of Player1's Scissors")
            player2Score += 1
            print(f"\nPlayer 1 score = {player1Score} \nPlayer 2 score = {player2Score} \n")

        elif player2Move=="S":
            print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
            print(f"\nPlayer 1 score = {player1Score} \nPlayer 2 score = {player2Score} \n")

        elif player2Move=="P":
            print("Player1's Scissors make confetti out of Player2's paper!")
            player1Score += 1
            print(f"\nPlayer 1 score = {player1Score} \nPlayer 2 score = {player2Score} \n ")

        else:
            print("Invalid Move Player 2!")
        continue
    else:
        print("Invalid Move Player 1!")
