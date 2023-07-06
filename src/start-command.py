import os
import sys


def clear_console():
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")
def save():
	text = ""
	for i in range (len(data)):
		for j in range(len(data[i])):
			text += str(data[i][j])
			if j + 1 != len(data[i]):
				text += ","
		text += "\n"
	file = open("data/config.txt", 'w')
	file.write(text)
	file.close()
	



f = open("data/config.txt","r")
lines = f.readlines()
data = []
for i in range(len(lines)):
	lines[i] = lines[i].replace("\n","")
	data.append(lines[i].split(","))


def main():
	option = 0
	options = ["Fullscreen", "Normal"]
	import getch
	while True:
		for i in range ( len(options)):
			if option == i:
				print("--> " + str(options[i]))
			else:
				print("    " + str(options[i]))
		mod = getch.getch()
		if mod == "W" or mod == "w":
			if option > 0:
				option -= 1
		elif mod == "S" or mod == "s":
			if option < len(options) - 1:
				option += 1
		
		if mod == "\n" or mod == " ":
			if option == 0:
				data[1][1] = 'true'
				break
			elif option == 1:
				data[1][1] = 'false'
				break
		clear_console()

	save()

if __name__ == "__main__":
	main()
	import game
	game.main()
