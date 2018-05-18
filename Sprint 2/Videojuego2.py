import sys
import time
import pygame
import pygameMenu
from random import randint
from random import randrange
from pygame.locals import *
from pygameMenu.locals import*

# TEXTO PARA LOS MENUS

# listaObjetos = []

SOBRE_NOSOTROS = ['- Alvaro  Alejandro  Nuñez  Mendoza',
				  '- Claudio  Lisandro  Mori  Rivas',
				  '- Alejandro  Javier  Ortiz  Balazar',
				  '- Julio  Cesar  Huaman  Mendoza',
				  '- Rodrigo Rene  Ramos  Vargas',
				  '- Percy  Javier  Moreno  Vasquez']

COMO_JUGAR = ['- Presiona  Izquierda / Derecha  para   moverte',
			  '- Presiona  Arriba  para  saltar',
			  '- Presiona  "ESC"  para  salir  del  juego']

# Variables globales
ancho = 640
alto = 800

# Tamaño del menu del juego y colores
color_fondo = (128, 0, 128)
color_negro = (0,0,0)
color_blanco = (255,255,255)
color_fondo_menu = (228, 55, 36)
tamaño_del_menu = (640, 480)

# Funciones del menú
def juego_terminado():
	fuente = pygame.font.SysFont('Consolas', 72)
	texto = fuente.render('Juego terminado', True, (255,255,255))
	texto_rect = texto.get_rect()
	texto_rect = [(ancho / 2) - 300, alto / 2]
	ventana.blit(texto, texto_rect)
	pygame.display.flip()
	# Pausamos
	time.sleep(3)
	# Salimos
	sys.exit()

def cambiar_dificultad():
	pass

def background():
	fondoMenu = pygame.image.load("menuPantalla.png")
	ventana.blit(fondoMenu,(0,0))

def color_random():
	return randrange(0, 255), randrange(0, 255), randrange(0, 255)

class CRunner():
	def ChasquiRunner(self):
		pygame.init()
		self.ventana = pygame.display.set_mode((ancho, alto))
		pygame.display.set_caption("Chasqui Runner")
		self.imagenFondo = pygame.image.load("Carretera_Ver1.png")
		pygame.key.set_repeat(20)

		pygame.mixer.music.load("game_music.mp3")
		pygame.mixer.music.play(3)

		self.jugador = Chasqui(alto-550,ancho-50)
		self.reloj = pygame.time.Clock()
		self.obstaculos1 = Obstaculo1(0,randrange(80,560))
		self.obstaculos2 = Obstaculo2(0,randrange(160,560))
		self.obstaculos3 = Obstaculo3(0,randrange(80,560))

		while True:

			# Una vez subida la lista de imagenes se pone el tiempo para determinar el cambio
			self.segundos = int(pygame.time.get_ticks()/1000.0)
			# Definir los FPS del videojuego
			self.reloj.tick(60)
			self.eventos = pygame.event.get()

			for self.evento in self.eventos:
				if self.evento.type == QUIT:
					pygame.quit()
					sys.exit()

				elif self.evento.type == pygame.KEYDOWN:
					if self.evento.key == K_LEFT:
						self.jugador.movimientoIzquierda()
					if self.evento.key == K_RIGHT:
						self.jugador.movimientoDerecha()

			self.ventana.blit(self.imagenFondo, (0,0))
			self.jugador.comportamiento(self.segundos)
			self.jugador.dibujar(self.ventana)
			
			self.obstaculos1.dibujar(self.ventana)
			self.obstaculos1.movimientoVertical()
			self.obstaculos2.dibujar(self.ventana)
			self.obstaculos2.movimientoVertical()
			self.obstaculos3.dibujar(self.ventana)
			self.obstaculos3.movimientoVertical()

			if pygame.sprite.collide_rect(self.obstaculos1, self.jugador):
				juego_terminado()
			if pygame.sprite.collide_rect(self.obstaculos2, self.jugador):
				juego_terminado()
			if pygame.sprite.collide_rect(self.obstaculos3, self.jugador):
				juego_terminado()


			pygame.display.update()

# Programación del Chusqui Runner
class Chasqui(pygame.sprite.Sprite):
	def __init__(self,posx,posy):
		pygame.sprite.Sprite.__init__(self)

		# Se va a hacer un cambio de todas las imagenes debido a que el chasqui va a tener que correr de forma dinámica, no estática
		
		self.imagen1 = pygame.image.load(r"model-chasqui\sprite_Chasqui00.png")
		self.imagen2 = pygame.image.load(r"model-chasqui\sprite_Chasqui01.png")
		self.imagen3 = pygame.image.load(r"model-chasqui\sprite_Chasqui02.png")
		self.imagen4 = pygame.image.load(r"model-chasqui\sprite_Chasqui03.png")
		self.imagen5 = pygame.image.load(r"model-chasqui\sprite_Chasqui04.png")
		self.imagen6 = pygame.image.load(r"model-chasqui\sprite_Chasqui05.png")
		self.imagen7 = pygame.image.load(r"model-chasqui\sprite_Chasqui06.png")
		self.imagen8 = pygame.image.load(r"model-chasqui\sprite_Chasqui07.png")
		self.imagen9 = pygame.image.load(r"model-chasqui\sprite_Chasqui08.png")
		self.imagen10 = pygame.image.load(r"model-chasqui\sprite_Chasqui09.png")
		self.imagen11 = pygame.image.load(r"model-chasqui\sprite_Chasqui10.png")
		"""
		self.imagen1 = pygame.image.load(r"model-chasqui\sprite_00.png")
		self.imagen2 = pygame.image.load(r"model-chasqui\sprite_01.png")
		self.imagen3 = pygame.image.load(r"model-chasqui\sprite_02.png")
		self.imagen4 = pygame.image.load(r"model-chasqui\sprite_03.png")
		self.imagen5 = pygame.image.load(r"model-chasqui\sprite_04.png")
		self.imagen6 = pygame.image.load(r"model-chasqui\sprite_05.png")
		self.imagen7 = pygame.image.load(r"model-chasqui\sprite_06.png")
		self.imagen8 = pygame.image.load(r"model-chasqui\sprite_07.png")
		self.imagen9 = pygame.image.load(r"model-chasqui\sprite_08.png")
		self.imagen10 = pygame.image.load(r"model-chasqui\sprite_09.png")
		self.imagen11 = pygame.image.load(r"model-chasqui\sprite_10.png")"""

		# Luego esto se va a agregar a una lista para asi poder recorrerla y generar el movimiento del personaje
		self.listaImagenes = [self.imagen1, self.imagen2, self.imagen3, self.imagen4,
							  self.imagen5, self.imagen6, self.imagen7, self.imagen8,
							  self.imagen9, self.imagen10, self.imagen11]
		self.posImagen = 0

		# Se pone la imagen encime del fondo
		self.imagenesPosicion = self.listaImagenes[self.posImagen]
		self.rect = self.imagenesPosicion.get_rect()

		# Sirve para recorrer la imagen de acuerdo al tiempo que se le otorque
		self.tiempoCambio = 1

		# Verificar si el jugador perdio
		self.partidaPerdida = False

		# La velocidad en la cual ira el chasqui
		self.velocidad = 5
		self.rect.top = posy
		self.rect.left = posx

	def dibujar(self, superficie):
		self.imagenesPosicion = self.listaImagenes[self.posImagen]
		superficie.blit(self.imagenesPosicion, self.rect)

	def comportamiento(self, tiempo):
		# En esta funcion se recorre la lista para hacer el cambio de imágenes y asi generar el movimiento
		if self.tiempoCambio == tiempo:
			self.posImagen += 1
			self.tiempoCambio += 1

			if self.posImagen > len(self.listaImagenes)-1:
				self.posImagen = 0

	def movimientoDerecha(self):
		self.rect.right += self.velocidad
		self.__movimiento()

	def movimientoIzquierda(self):
		self.rect.left -= self.velocidad
		self.__movimiento()

	def __movimiento(self):
		if self.rect.left <= 40:
			self.rect.left = 50
		elif self.rect.right > 600:
			self.rect.right = 590

class Obstaculo1(pygame.sprite.Sprite):
	def __init__(self, posy, posx):
		pygame.sprite.Sprite.__init__(self)

		self.imagen = pygame.image.load("obstaculo1.png")
		self.rect = self.imagen.get_rect()

		self.validacion = 1

		self.velocidad = 6
		self.rect.top = posy
		self.rect.left = posx

	def dibujar(self, superficie):
		superficie.blit(self.imagen, self.rect)

	def movimientoVertical(self):
		self.rect.top = self.rect.top + self.velocidad
		self.__repeticion()

	def __repeticion(self):
		if self.rect.top + 50 > alto:
			self.rect.top = -100

class Obstaculo2(pygame.sprite.Sprite):
	def __init__(self, posy, posx):
		pygame.sprite.Sprite.__init__(self)

		self.imagen = pygame.image.load("obstaculo2.png")
		self.rect = self.imagen.get_rect()

		self.validacion = 1

		self.velocidad = 4
		self.rect.top = posy
		self.rect.left = posx

	def dibujar(self, superficie):
		superficie.blit(self.imagen, self.rect)

	def movimientoVertical(self):
		self.rect.top = self.rect.top + self.velocidad
		self.__repeticion()

	def __repeticion(self):
		if self.rect.top + 50 > alto:
			self.rect.top = -100

class Obstaculo3(pygame.sprite.Sprite):
	def __init__(self, posy, posx):
		pygame.sprite.Sprite.__init__(self)

		self.imagen = pygame.image.load("obstaculo3.png")
		self.rect = self.imagen.get_rect()

		self.validacion = 1

		self.velocidad = 7
		self.rect.top = posy
		self.rect.left = posx

	def dibujar(self, superficie):
		superficie.blit(self.imagen, self.rect)

	def movimientoVertical(self):
		self.rect.top = self.rect.top + self.velocidad
		self.__repeticion()

	def __repeticion(self):
		if self.rect.top + 50 > alto:
			self.rect.top = -100



#    -----   MENU   -----
# MENU DEL JUEGO
class GameMenu():
	def menu_del_juego(self):
		self.menu_jugar = pygameMenu.Menu(ventana,
			                            bgfun=background,
			                            color_selected=color_blanco,
			                            font=pygameMenu.fonts.FONT_BEBAS,
			                            font_color=color_negro,
			                            font_size=30,
			                            menu_alpha=0,
			                            menu_height=int(tamaño_del_menu[1]),
			                            menu_width=int(tamaño_del_menu[0]),
			                            onclose=PYGAME_MENU_DISABLE_CLOSE,
			                            option_shadow=False,
			                            title='Menu Principal',
			                            window_height=tamaño_del_menu[1],
			                            window_width=tamaño_del_menu[0]
			                            )

		self.menu_jugar.add_option('Empezar!', game.ChasquiRunner)
		self.menu_jugar.add_selector('Poner dificultad', [('Facil', 'FACIL'),
													 ('Medio', 'MEDIO'),
													 ('Dificil', 'DIFICIL')],
								onreturn = False,
								onchange = cambiar_dificultad)
		self.menu_jugar.add_option('Salir', PYGAME_MENU_BACK)

	# MENU SOBRE NOSOTROS
		self.menu_sobre_nosotros = pygameMenu.TextMenu(ventana,
					                            bgfun=background,
					                            color_selected=color_blanco,
					                            font=pygameMenu.fonts.FONT_BEBAS,
					                            font_color=color_negro,
					                            font_size=30,
					                            menu_alpha=0,
					                            menu_height=int(tamaño_del_menu[1]),
					                            menu_width=int(tamaño_del_menu[0]),
					                            onclose=PYGAME_MENU_DISABLE_CLOSE,
					                            option_shadow=False,
					                            title='SOBRE NOSOTROS',
					                            window_height=tamaño_del_menu[1],
					                            window_width=tamaño_del_menu[0]
					                            )
		self.menu_sobre_nosotros.add_option("REGRESAR AL MENU PRINCIPAL", PYGAME_MENU_BACK)
		for self.m in SOBRE_NOSOTROS:
			self.menu_sobre_nosotros.add_line(self.m)
		self.menu_sobre_nosotros.add_line(PYGAMEMENU_TEXT_NEWLINE)

	# MENU COMO JUGAR
		self.menu_como_jugar = pygameMenu.TextMenu(ventana,
				                            bgfun=background,
				                            color_selected=color_blanco,
				                            font=pygameMenu.fonts.FONT_BEBAS,
				                            font_color=color_negro,
				                            font_size=30,
				                            menu_alpha=0,
				                            menu_height=int(tamaño_del_menu[1] ),
				                            menu_width=int(tamaño_del_menu[0]),
				                            onclose=PYGAME_MENU_DISABLE_CLOSE,
				                            option_shadow=False,
				                            title='COMO JUGAR',
				                            window_height=tamaño_del_menu[1],
				                            window_width=tamaño_del_menu[0]
				                            )
		self.menu_como_jugar.add_option("REGRESAR AL MENU PRINCIPAL", PYGAME_MENU_BACK)
		for self.m in COMO_JUGAR:
			self.menu_como_jugar.add_line(self.m)
		self.menu_como_jugar.add_line(PYGAMEMENU_TEXT_NEWLINE)

	# MENU PRINCIPAL
		self.menu_principal = pygameMenu.Menu(ventana,
			                            bgfun=background,
			                            color_selected=color_blanco,
			                            font=pygameMenu.fonts.FONT_BEBAS,
			                            font_color=color_negro,
			                            font_size=30,
			                            menu_alpha=0,
			                            menu_height=int(tamaño_del_menu[1]),
			                            menu_width=int(tamaño_del_menu[0]),
			                            onclose=PYGAME_MENU_DISABLE_CLOSE,
			                            option_shadow=False,
			                            title='Menu Principal',
			                            window_height=tamaño_del_menu[1],
			                            window_width=tamaño_del_menu[0]
			                            )

		self.menu_principal.add_option('Empezar Juego', self.menu_jugar)
		self.menu_principal.add_option('Sobre Nosotros', self.menu_sobre_nosotros)
		self.menu_principal.add_option('Como jugar', self.menu_como_jugar)
		self.menu_principal.add_option('Salir', PYGAME_MENU_EXIT)

		# Loop del menu
		while True:
			# FPS DEL JUEGO
			clock.tick(60)
			# Eventos del menu
			eventos = pygame.event.get()
			for evento in eventos:
				if evento.type == QUIT:
					pygame.quit()
					sys.exit()

			# MENU PRINCIPAL
			self.menu_principal.mainloop(eventos)

			# Flip
			pygame.display.flip()


# INICIALIZACIÓN DEL JUEGO
pygame.init()

game = CRunner()

ventana = pygame.display.set_mode(tamaño_del_menu)
pygame.display.set_caption("CHASQUI RUNNER MENU")
clock = pygame.time.Clock()

# Comenzamos a llamar a la clase GameMenu para inicializar el Menú del juego
game_menu = GameMenu()
game_menu.menu_del_juego()