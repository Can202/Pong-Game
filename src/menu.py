import pygame
from variables import THEFONT, THEFONTBIG, FIXED_HEIGHT, FIXED_WIDTH
clock = pygame.time.Clock()

pygame.font.init()
text_title = THEFONTBIG.render('Pong', False, (255, 255, 255))
text_play = THEFONT.render('Press Space', False, (255, 255, 255))
def main(screen, sc_w, sc_h):
	global clock
	#draw
	screen.fill("black")
	text_title_width = fixW(583, sc_w)
	text_title_height = fixH(250, sc_h)
	text_play_width = fixW(583, sc_w)
	text_play_height = fixH(400, sc_h)
	screen.blit(text_title, (text_title_width,text_title_height))
	screen.blit(text_play, (text_play_width,text_play_height))
	
	#mod
	keys = pygame.key.get_pressed()
	if keys[pygame.K_SPACE]:
		return 1
	elif keys[pygame.K_ESCAPE]:
		return 2
	
	#update
	pygame.display.flip()
	deltaTime = clock.tick(60) / 1000
	
	return 0
	

def fixW(number, sc_width):
	real_number = (number / FIXED_WIDTH) * sc_width
	return real_number
	
def fixH(number, sc_height):
	real_number = (number / FIXED_HEIGHT) * sc_height
	return real_number
	
