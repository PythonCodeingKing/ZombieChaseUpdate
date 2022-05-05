import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, zombieGame):
		super().__init__()
		self.screen = zombieGame.screen
		self.image = pygame.image.load("images/player.png")
		self.rect = self.image.get_rect()
		
		self.score = 0
		self.health = 100
	def draw(self):
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		x, y = pygame.mouse.get_pos()
		
		self.rect.x = x
		self.rect.y = y
