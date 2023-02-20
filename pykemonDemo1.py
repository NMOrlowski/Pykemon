# pykemonDemo1.py
# This is a demo to learn pygame. It will draw a window and produce the gameboy console family "Gameboy" logo from startup

import pygame
from pygame.locals import *
from pygame import mixer
 
pygame.init()
mixer.init()
vec = pygame.math.Vector2
 
HEIGHT = 576
WIDTH = 640
FPS = 60
 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pykemon")

logoImg = pygame.image.load('GB Nintendo boot logo.png')

def logo(x, y):
	displaysurface.blit(logoImg, (x,y))

x = (112)
y = (0)

def bootSound():
	pygame.mixer.music.load('GB Nintendo boot sound.wav')
	pygame.mixer.music.play()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	displaysurface.fill((255,255,255))

	logo(x,y)

	if y < 256:
		y += 1.25
		if y == 250:
			bootSound()

	pygame.display.update()
	FramePerSec.tick(FPS)