import pygame
from pygame.sprite import Sprite

import random

class Star(Sprite):
	def __init__(self, chase):
		super().__init__()
		self.screen = chase.screen
		self.player = chase.player
		self.image = pygame.image.load("images/star.png")
		self.rect = self.image.get_rect()
		self.rect.y = random.randint(0, 590)
		self.rect.x = random.randint(0, 590)

	def draw(self):
		self.screen.blit(self.image, self.rect)
	
	def update(self):
		if pygame.sprite.collide_rect(self.player, self):
			self.rect.y = random.randint(0, 590)
			self.rect.x = random.randint(0, 590)
			self.player.score += 1
