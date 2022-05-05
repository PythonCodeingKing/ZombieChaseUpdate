import hashlib
import getpass
import pygame

from player import Player
from zombie import Zombie
from button import Button
from star import Star

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((600, 600))
		pygame.display.set_caption("Zombie Chase! (UPDATE 4!)")
		self.player = Player(self)
		self.zombies = pygame.sprite.Group()
		
		pygame.mouse.set_visible(True)
		self.ticks = 1
		self.play_button = Button(self, "Play")
		self.debug = False
		self.game_active = False
		self.clock = pygame.time.Clock()
		self.star = Star(self)
		self.run_game()
		
	def run_game(self):
		self.clock.tick(60)
		while 1:
			# this is run every frame
			if self.game_active:
				self.player.update()
				self.collisions()
				self.clock.tick(60)
				self.update_tickspeed()
				self.star.update()
				self.zombies.update()
			self.check_events()
			self.update_screen()
	def update_tickspeed(self):
		self.ticks += 1
		if (self.ticks % 60) == 0:
			self.zombies.add(Zombie(self))
		if (self.ticks % int(self.clock.get_fps() + 1)) == 0:
			for zombie in self.zombies.copy():
				zombie.seconds -= 1
				if zombie.seconds == 0:
					self.zombies.remove(zombie)
		if self.ticks >= 10000000:
			self.ticks = 1
	
	def collisions(self):
		
		if pygame.sprite.spritecollideany(self.player, self.zombies):
				self.player.health -= 10
				self.player.score = 0
				self.zombies.empty()
				if self.player.health <= 0:
					self.game_active = False
					self.player = Player(self)
	def draw_text(self):
		# draw the stats board
		font = pygame.font.SysFont("Monospace", 24)
			
		img = font.render(f'P1 Health: {self.player.health}', True, (255, 0, 0))
		self.screen.blit(img, (0, 0))
		img = font.render(f'P1 Score: {self.player.score}', True, (255, 0, 0))
		self.screen.blit(img, (0, 10))
		if self.debug:
			img2 = font.render(f'FPS: {int(self.clock.get_fps())}', True, (255, 0, 0))
			self.screen.blit(img2, (0, 25))
			img2 = font.render(f'Player Coord: {self.player.rect.x}, {self.player.rect.y}', True, (255, 0, 0))
			self.screen.blit(img2, (0, 40))
			img2 = font.render(f'Zombies: {len(self.zombies)}', True, (255, 0, 0))
			self.screen.blit(img2, (0, 55))

	def update_screen(self):
		
		self.screen.fill((0, 0, 230))
		if self.game_active:
			for zombie in self.zombies.sprites():
				zombie.draw()
			pygame.mouse.set_visible(False)
			self.player.draw()
			self.star.draw()
			self.draw_text()
			

		else:
			self.play_button.draw()
			pygame.mouse.set_visible(True)
		pygame.display.flip()
		
	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_f:
					self.debug = not self.debug
				if event.key == pygame.K_k:
					self.player.health = 0
					self.game_active = False
				if event.key == pygame.K_q:
					quit()
			if event.type == pygame.MOUSEBUTTONDOWN and not self.game_active:
				if self.play_button.check_button():
					self.game_active = True
			if event.type == pygame.QUIT:
				quit()
			
if __name__ == "__main__":
	password = getpass.getpass()
	print("encoding")
	message = password.encode('utf-8')
	alg = hashlib.sha256()
	print("encrypting")
	alg.update(message)
	hashpass = alg.hexdigest()
	with open("authentication.txt","r") as f:
		if f.read() == hashpass:
			print("done.")
			game = Game()
		else:
			print("Wrong password. Please try again.")