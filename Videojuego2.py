import pygame
import sys
from pygame.locals import *

# Variables globales
ancho = 640
alto = 1000

class Combi(pygame.sprite.Sprite):
	def __init__(self, posx, posy):
		pygame.sprite.Sprite.__init__(self)

		self.imagen1 = pygame.image.load("C:\Software 2 Proyecto\is2_prueba\ProyectoSoftware\imagenes\combi.jpg")

		self.rect = self.imagen1.get_rect()

		self.velocidad = 10
		self.rect.top = posx
		self.rect.left = posy

	def dibujar(self, superficie):
		superficie.blit(self.imagen1, self.rect)

pygame.init()
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("CombiRacer")
imagenFondo = pygame.image.load("C:\Software 2 Proyecto\is2_prueba\ProyectoSoftware\imagenes\pantallaNegro.jpg")

jugador = Combi(ancho/2,alto-800)

reloj = pygame.time.Clock()

while True:

	# Definir los FPS del videojuego
	reloj.tick(60)

	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()

		elif evento.type == pygame.KEYDOWN:
			if evento.key == K_LEFT:
				jugador.rect.left -= jugador.velocidad
			if evento.key == K_RIGHT:
				jugador.rect.right += jugador.velocidad
			if evento.key == K_UP:
				jugador.rect.top -= jugador.velocidad
			if evento.key == K_DOWN:
				jugador.rect.bottom +=jugador.velocidad

	ventana.blit(imagenFondo, (0,0))

	jugador.dibujar(ventana)

	pygame.display.update()