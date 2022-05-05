import random
import pygame

class Zombie(pygame.sprite.Sprite):
	def __init__(self, chase):
		super().__init__()
		self.screen = chase.screen
		self.player_rect = chase.player.rect
		self.image = pygame.image.load("images/zombie.png")
		self.rect = self.image.get_rect()
		random.seed()
		self.speed = 0.5
		self.rect.x = random.randint(0, 600)
		self.rect.y = random.randint(0, 600)
		self.seconds = 10
		self.last_dir = None
	def draw(self):
		self.screen.blit(self.image, self.rect)
	
	def update(self):
		x = self.rect.x
		y = self.rect.y
		rect = self.player_rect
		if x < rect.x:
			x += 1
		if x > rect.x:
			x -= 1
		if y < rect.y:
			y += 1
		if y > rect.y:
			y -= 1
		self.rect.x = x
		self.rect.y = y
			
			
			
