import pygame
import random

from variables import *
import menu

def main():
	global running, playing
	global deltaTime
	global sc_width
	global sc_height
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		if playing:
			# Draw
			draw()
			# Modification
			keys = pygame.key.get_pressed()
			modification(keys)
			# Update
			update()
		else:
			result = menu.main(screen, sc_width, sc_height)
			if result == 1:
				restart_everything()
			elif result == 2:
				running = False

def draw():
	global screen
	global player_1, player_2, ball
	screen.fill("black")
	#pygame.draw.rect(screen,"white",(200,150,100,50))
	pygame.draw.rect(screen, player_1.color, player_1.rect)
	pygame.draw.rect(screen, player_2.color, player_2.rect)
	pygame.draw.ellipse(screen, ball.color, ball.rect)

def modification(keys):
	global running, first_move
	global player_1, player_2
	global deltaTime
	
	if keys[pygame.K_ESCAPE]:
		running = False
	
	# Player 1
	if keys[pygame.K_w]:
		if player_1.top > 0:
			player_1.top -= player_1.velocity * deltaTime
			first_move = True
	if keys[pygame.K_s]:
		if player_1.bottom < (FIXED_HEIGHT):
			player_1.top += player_1.velocity * deltaTime
			first_move = True
	# Player 2
	if keys[pygame.K_UP]:
		if player_2.top > 0:
			player_2.top -= player_2.velocity * deltaTime
			first_move = True
	if keys[pygame.K_DOWN]:
		if player_2.bottom < (FIXED_HEIGHT):
			player_2.top += player_2.velocity * deltaTime
			first_move = True
			

def update():
	global sc_width, sc_height, deltaTime, playing, first_move
	global player_1, player_2, ball
	
	
	player_1.update()
	player_2.update()
	if first_move:
		ball.update()
		ball.collide_with(player_1)
		ball.collide_with(player_2)
	else:
		ball.update(movement = False)
	
	if ball.collide_with_the_wall != 0:
		playing = False
	
	
	sc_width, sc_height = pygame.display.get_surface().get_size()
	pygame.display.flip()
	deltaTime = clock.tick(60) / 1000


def fixW(number):
	global sc_width
	real_number = (number / FIXED_WIDTH) * sc_width
	return real_number
	
def fixH(number):
	global sc_height
	real_number = (number / FIXED_HEIGHT) * sc_height
	return real_number
	

class Base():
	def __init__(self):
		#Rect(left, top, width, height)
		self.width = 25
		self.height = 150
		self.left = 50
		self.top = (FIXED_HEIGHT - self.height) / 2
		self.rect = pygame.Rect(fixW(self.left),fixH(self.top), fixW(self.width), fixH(self.height))
		self.bottom = self.top + self.height
		self.right = self.left + self.width
		
		self.velocity = 500
		self.color = "white"
		
	def update(self):
		self.rect = pygame.Rect(fixW(self.left),fixH(self.top), fixW(self.width), fixH(self.height))
		self.bottom = self.top + self.height
		self.right = self.left + self.width
		self.centerW = (self.left + self.right) / 2
		self.centerH = (self.top + self.bottom) / 2
class Player(Base):
	pass
class Ball(Base):
	def __init__(self):
		Base.__init__(self)
		self.width = 40
		self.height = 40
		self.left = (FIXED_WIDTH - self.width) / 2
		self.top = (FIXED_HEIGHT - self.height) / 2
		self.rect = pygame.Rect(fixW(self.left),fixH(self.top), fixW(self.width), fixH(self.height))
		
		self.velocity = 500
		
		self.facing_x = random.choice([-1,1])
		self.facing_y = random.choice([-1,1])
		
		self.collide_with_the_wall = 0
		
	def update(self, movement = True):
		global deltaTime, sc_width, sc_height
		Base.update(self)
		if movement:
			self.left += self.velocity * self.facing_x * deltaTime
			self.top += self.velocity * self.facing_y * deltaTime
			if self.left <= 0 and self.facing_x == -1:
				self.facing_x = 1
				self.collide_with_the_wall = -1
			elif self.right >= FIXED_WIDTH and self.facing_x == 1:
				self.facing_x = -1
				self.collide_with_the_wall = 1
			if self.top <= 0 and self.facing_y == -1:
				self.facing_y = 1
			elif self.bottom >= FIXED_HEIGHT and self.facing_y == 1:
				self.facing_y = -1
	def collide_with(self, other):
		
		col_left = other.right > self.left and other.left < self.left
		col_right = other.left < self.right and other.right > self.right
		col_top = other.top < self.top and other.bottom > self.top
		col_bottom =  other.bottom > self.bottom and other.top < self.bottom
		col_centerW = other.right > self.centerW and other.left < self.centerW
		
		# Collide from the left
		if self.facing_x == -1 and col_left and col_top:
			self.facing_x = 1
		if self.facing_x == -1 and col_left and col_bottom:
			self.facing_x = 1
			
		# Collide from the right
		if self.facing_x == 1 and col_right and col_top:
			self.facing_x = -1
		if self.facing_x == 1 and col_right and col_bottom:
			self.facing_x = -1
			
		# Collide from the bottom
		if self.facing_y == 1 and col_bottom and col_centerW:
			self.facing_y = -1
			#doesnt make sense, but to the game
			self.facing_x *= -1
		
		# Collide from the top
		if self.facing_y == -1 and col_top and col_centerW:
			self.facing_y = 1
			#doesnt make sense, but to the game
			self.facing_x *= -1
		


clock = pygame.time.Clock()
ball = Ball()
player_1 = Player()
player_2 = Player()
player_1.left = 50
player_2.left = FIXED_WIDTH - player_2.width - 50
first_move = False
sc_width = 1366
sc_height = 720

def restart_everything():
	global playing, ball, player_1, player_2, deltaTime, first_move
	playing = True
	ball.__init__()
	player_1.__init__()
	player_2.__init__()
	player_1.left = 50
	player_2.left = FIXED_WIDTH - player_2.width - 50
	deltaTime = 0
	first_move = False

if __name__ == "__main__":
	main()
