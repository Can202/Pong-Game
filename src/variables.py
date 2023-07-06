import pygame
FIXED_WIDTH = 1366
FIXED_HEIGHT = 720
'''
sc_width = 1366
sc_height = 720
'''

f = open("data/config.txt","r")
lines = f.readlines()

data = []
for i in range(len(lines)):
	lines[i] = lines[i].replace("\n","")
	data.append(lines[i].split(","))


sc_width = float(data[0][1])
sc_height = float(data[0][2])
running = True
playing = True
deltaTime = 0

pygame.init()
pygame.font.init()

THEFONTBIG = pygame.font.Font('data/fonts/font.otf', 70)
THEFONT = pygame.font.Font('data/fonts/font.otf', 30)

if data[1][1] == 'true':
	screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
	screen = pygame.display.set_mode((sc_width, sc_height), pygame.RESIZABLE)


