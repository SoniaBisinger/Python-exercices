# Done for Replit

# from replit import audio
import os, time


def play():
	source = audio.play_file('audio.wav')
	source.paused = False  # unpause the playback


while True:
	# clear the screen
	os.system("clear")
	# Show the menu
	print("🎵 MyPOD Music Player")
	print("Press 1 to Play")
	print("Press 2 to Exit")
	print("\nPress anything else to see the menu again.")
	time.sleep(2)
	os.system("clear")
	# take user's input
	choice = int(input())
	# check whether you should call the play() subroutine depending on user's input
	if choice == 1:
		play()
	elif choice == 2:
		break
	else:
		continue
