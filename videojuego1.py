import pygame
import sys


ancho = 640
alto = 480

'4. Creando la bolita'
class Bolita(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
 
		'Cargar imagen'
		self.image = pygame.image.load('C:/Documentos/Pygame/Ladrillos/bolita.png')
		
		self.rect = self.image.get_rect()

		'7. posicion inicial centrada en pantalla'
		self.rect.centerx = ancho /2
		self.rect.centery = alto /2


'1. Estableciendo pantalla'
pantalla = pygame.display.set_mode((ancho, alto))

'3. Configurando titulo'
pygame.display.set_caption('Juego de Ladrillos')

'5. Creamos bolita en base a nuestra nueva clase Bolita'
bolita = Bolita()

'2. Hacer que la ventana permanezca abierta'
while True:
	'Revisar todos los eventos'
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			sys.exit()

	'6. dibujar bolita'		
	pantalla.blit(bolita.image, bolita.rect)

    
	pygame.display.flip()

