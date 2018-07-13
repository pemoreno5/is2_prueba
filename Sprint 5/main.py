import sys
import os
import time
import pygame
import lib.pygameMenu as pygameMenu
from random import randint
from random import randrange
from pygame.locals import *
from lib.pygameMenu.locals import*

# TEXTO PARA LOS MENUS
SOBRE_NOSOTROS = ['- Alvaro  Alejandro  Nuñez  Mendoza',
				  '- Claudio  Lisandro  Mori  Rivas',
				  '- Alejandro  Javier  Ortiz  Balazar',
				  '- Julio  Cesar  Huaman  Mendoza',
				  '- Rodrigo Rene  Ramos  Vargas',
				  '- Percy  Javier  Moreno  Vasquez']

COMO_JUGAR = ['- Presiona  Izquierda / Derecha  para   moverte',
			  '- Presiona  Arriba  para  saltar',
			  '- Presiona  "ESC"  para  salir  del  juego']

PAUSA = ['REGRESAR AL JUEGO']

# Variables globales
ancho = 640
alto = 800
SKIN = ['DEFAULT-EASY']
eventoPausa = None

# Tamaño del menu del juego y colores
color_fondo = (128, 0, 128)
color_negro = (0,0,0)
color_blanco = (255,255,255)
color_fondo_menu = (228, 55, 36)
tamaño_del_menu = (640, 480)
JuegoCorriendo = True
MENU_CENTERED_TEXT = True

def tkinbuscar():
	pass

def cambiar_skin(d):
	print("Seleccionar Skin: {0}".format(d))
	SKIN[0] = d

def cambiar_dificultad(d):
	print("Seleccionar Dificultad: {0}".format(d))
	DIFICULTAD[0] = d

def funcion_skin(skin):
	skin = skin[0]
	# verificando si valor del objeto skin es string
	assert isinstance(skin, str)
	model = Chasqui(alto-550,ancho-50)

	#Cambiar dificultad

	if skin == 'DEFAULT-EASY' or skin == 'GOKU-EASY' or skin == 'HULK-EASY':
		print("Inicializado con dificultad {}".format(skin))
		if JuegoCorriendo == True:
			game.ChasquiRunner()
	elif skin == 'DEFAULT-MEDIUM' or skin == 'GOKU-MEDIUM' or skin == 'HULK-MEDIUM':
		print("Inicializado con dificultad {}".format(skin))
		if JuegoCorriendo == True:
			game.ChasquiRunner()
	elif skin == 'DEFAULT-HARD' or skin == 'GOKU-HARD' or skin == 'HULK-MEDIUM':
		print("Inicializado con dificultad {}".format(skin))
		if JuegoCorriendo == True:
			game.ChasquiRunner()
	else:
		raise Exception('Unknown skin {0}'.format(skin))

	'''if skin == 'DEFAULT-EASY' or skin == 'DEFAULT-MEDIUM' or skin == 'DEFAULT-HARD':
		print("Inicializado sin cambios")
		if JuegoCorriendo == True:
			game.ChasquiRunner()
	elif skin == 'GOKU-EASY' or skin == 'GOKU-MEDIUM' or skin == 'GOKU-HARD':
		print("Inicializado con cambios  {}".format(skin))
		if JuegoCorriendo == True:
			game.ChasquiRunner()
	elif skin == 'HULK-EASY' or skin == 'HULK-MEDIUM' or skin == 'HULK-HARD':
		print("Inicializado con cambios  {}".format(skin))
		if JuegoCorriendo == True:
			game.ChasquiRunner()
	else:
		raise Exception('Unknown skin {0}'.format(skin))'''
	
def juego_terminado():

	'''fuenteJT = pygame.font.SysFont('Consolas', 72)
	textoFondo, self.textoRect = text_objects("Pausa", self.fuenteJT)
	textoRect.center = ((ancho/2), (alto/2))
	ventana.blit(self.textoFondo, self.textoRect)
	
		while self.pausar:
			for self.evento in pygame.event.get():
				if self.evento.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
	
			self.ventana.fill((255,255,255))
	
			boton("Despausar",150, 450, 100, 50, (200,0,0), (255,0,0), self.__despausar)
			boton("Salir",550, 450, 100, 50, (0,220,0), (0,255,0), game_menu.menu_del_juego)
	
			pygame.display.update()
			clock.tick(15)'''
	# En esta función se va a poner "Juego terminado" una vez que el obstaculo
	# haya hecho collide con el chasqui y luego cerrara el juego 
	'''pygame.mixer.Sound('sonidos/mariobros_mushroomeffect.wav').set_volume(0.1)
	self.efecto_powerup2 = pygame.mixer.Sound("sonidos/mariobros_mushroomeffect.wav")
	self.efecto_powerup2.play()'''
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

def text_objects(texto, fuente):
	# Esta solo es una funcion para poner el texto de color negro, para poder
	# simplificar mas las funciones
	textoSurface = fuente.render(texto,True,(0,0,0))
	return textoSurface, textoSurface.get_rect()

def boton(mensaje, x, y, w, h, color1, color2, accion=None):
	# Esto sirve para crear botones con determinadas funciones, en este caso lo hemos
	# usado para crear los botones al momento de apretar la tecla "p", en el cual
	# cuando se haga clic, va a activar una determinada accion gracias a los parametros
	# de la función boton
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(ventana, color1, (x, y, w, h))
		if click[0] == 1 and accion != None:
			if accion == game_menu.menu_del_juego:
				pygame.mixer.music.stop()
				accion()
			else:
				accion()
	else:
		pygame.draw.rect(ventana, color2, (x, y, w, h))

	textito = pygame.font.SysFont('Consolas', 20)
	textoFondo, textoRect = text_objects(mensaje, textito)
	textoRect.center = ((x+(w/2)), (y+(h/2)))
	ventana.blit(textoFondo, textoRect)

def background():
	# Fonde del menu del juego
	fondoMenu = pygame.image.load("MPfondo.jpg")
	ventana.blit(fondoMenu,(0,0))

def color_random():
	return randrange(0, 255), randrange(0, 255), randrange(0, 255)


class CRunner():

	def ChasquiRunner(self):
		# Aca se empieza a correr el juego y definir los tamaños mas los nombres y la imagen de fondo
		pygame.init()
		self.ventana = pygame.display.set_mode((ancho, alto))

		self.mostrar_texto_velocidad = False
		self.mostrar_texto_escudo = False
		
		self.powerups = pygame.sprite.Group()
		self.todoslossprites = pygame.sprite.Group()
		pygame.display.set_caption("Chasqui Runner")
		self.imagenFondo = pygame.image.load("menuPantalla.png")

		# Sirve para que la imagen se mueva tan solo mantener apretada la tecla
		pygame.key.set_repeat(20)
		# Sirve para poner la musica en el juego
		pygame.mixer.music.load("sonidos/dbsuper_ultrainstinct_2.mp3")
		pygame.mixer.music.play(-1)

		# Se define la clase Chasqui con el nombre de "jugador"
		self.jugador = Chasqui(alto-550,ancho-50)
		self.todoslossprites.add(self.jugador)
		#self.powerups.add(self.jugador)
		self.reloj = pygame.time.Clock()
		# Se definen los 3 distintos obstaculos con determinadas zonas donde se va a caer los obstaculos
		self.obstaculos1 = Obstaculo1(0,randrange(80,560))
		self.todoslossprites.add(self.obstaculos1)
		self.obstaculos2 = Obstaculo2(0,randrange(160,560))
		self.todoslossprites.add(self.obstaculos2)
		self.obstaculos3 = Obstaculo3(0,randrange(80,560))
		self.todoslossprites.add(self.obstaculos3)

		self.powerup1 = PowerUp1(0,randrange(80,560))
		self.todoslossprites.add(self.powerup1)
		self.powerup2 = PowerUp2(0,randrange(160,560))
		self.todoslossprites.add(self.powerup2)         

		#self.powerup3 = PowerUp3(0,randrange(80,560))

		self.cmbdor = 5000
		self.pausar = False
		self.score = 0
		self.cont = 0
		# las vidas serán un valor numérico.
		self.vidas = 3
		#se usará 100 que representará al 100%. el símbolo de % se le añadirá por concatenación en la función que se muestra las vidas.
		#self.vidas = 100
		self.vivo = True

		while True:
			# Una vez subida la lista de imagenes se pone el tiempo para determinar el cambio
			self.segundos = int(pygame.time.get_ticks()/1000.0)
			self.score += self.segundos
			# Definir los FPS del videojuego
			self.reloj.tick(60)
			# Define los eventos que se van a hacer durante el juego
			self.eventos = pygame.event.get()
			for self.evento in self.eventos:
				if self.evento.type == QUIT:
					pygame.quit()
					sys.exit()
					# Se asignan las teclas para poder movilizar al chasqui
				elif self.evento.type == pygame.KEYDOWN:
					if self.evento.key == K_LEFT:
						self.jugador.movimientoIzquierda()
					if self.evento.key == K_RIGHT:
						self.jugador.movimientoDerecha()
					if self.evento.key == K_p:
						self.pausar = True
						self.cont += 1
						self.__pausa()
						if self.cont == 2:
							self.pausar = False
							self.__despausar()

			# Se define la imagen de fondo del juego
			self.ventana.blit(self.imagenFondo, (0,0))
			# Se define el movimiento del Chasqui o jugador
			self.jugador.comportamiento(self.segundos)
			# Y se dibuja en la pantalla
			self.jugador.dibujar(self.ventana)

			if self.obstaculos1 == None:
				self.obstaculos1 = Obstaculo1(0,randrange(80,560))
			if self.obstaculos2 == None:
				self.obstaculos2 = Obstaculo2(0,randrange(160,560))
			if self.obstaculos3 == None:
				self.obstaculos3 = Obstaculo3(0,randrange(80,560))                                            
			if self.powerup1 == None:
				self.powerup1 = PowerUp1(0,randrange(80,560))
			if self.powerup2 == None:
				self.powerup2 = PowerUp2(0,randrange(160,560))
			
			
			# Aca se definen los distintos obstaculos en la ventana con su movimiento asignado
			self.obstaculos1.dibujar(self.ventana)
			self.obstaculos1.movimientoVertical()
			self.obstaculos1.comportamiento(self.segundos)
			self.obstaculos2.dibujar(self.ventana)
			self.obstaculos2.movimientoVertical() 
			self.obstaculos2.comportamiento(self.segundos)
			self.obstaculos3.dibujar(self.ventana)
			self.obstaculos3.movimientoVertical()
			self.obstaculos3.comportamiento(self.segundos)
			self.powerup1.dibujar(self.ventana)
			self.powerup1.movimientoVertical()
			self.powerup2.dibujar(self.ventana) 
			self.powerup2.movimientoVertical()

			self.jugador_rect = pygame.Rect(self.jugador)

			# Define que se va a hacer al momento de que se origine un Collide
			if pygame.sprite.collide_rect(self.obstaculos1, self.jugador):
				self.__tipochoque1()
				self.obstaculos1.velocidad = self.obstaculos1.velocidad + 10
				self.vidas = self.vidas - 1
				if self.vidas == 0:
					juego_terminado()
			if self.obstaculos1 and self.jugador_rect.colliderect(self.obstaculos1.rect):
				self.todoslossprites.remove(self.obstaculos1)
				self.obstaculos1 = None

			if pygame.sprite.collide_rect(self.obstaculos2, self.jugador):
				self.__tipochoque2()
				self.obstaculos2.velocidad = self.obstaculos2.velocidad + 10
				self.vidas = self.vidas - 1
				if self.vidas == 0:
					juego_terminado()
			if self.obstaculos2 and self.jugador_rect.colliderect(self.obstaculos2.rect):
				self.todoslossprites.remove(self.obstaculos2)
				self.obstaculos2 = None

			if pygame.sprite.collide_rect(self.obstaculos3, self.jugador):
				self.__tipochoque2()
				self.obstaculos3.velocidad = self.obstaculos3.velocidad + 10
				self.vidas = self.vidas - 1
				if self.vidas == 0:
					juego_terminado()
			if self.obstaculos3 and self.jugador_rect.colliderect(self.obstaculos3.rect):
				self.todoslossprites.remove(self.obstaculos3)
				self.obstaculos3 = None

			if pygame.sprite.collide_rect(self.jugador, self.powerup1):
				self.__heart()
				self.mostrar_texto_escudo = True
				self.tiempoi_tescudo = pygame.time.get_ticks()
			if self.mostrar_texto_escudo:
				self.ventana.blit(self.textoE, self.texto_rectE)
				if pygame.time.get_ticks() - self.tiempoi_tescudo > 500:
					self.mostrar_texto_escudo = False
			if self.powerup1 and self.jugador_rect.colliderect(self.powerup1.rect):
				self.todoslossprites.remove(self.powerup1)
				self.powerup1 = None


			if pygame.sprite.collide_rect(self.jugador, self.powerup2):
				self.__speed()
				self.mostrar_texto_velocidad = True
				self.tiempoi_tvelocidad = pygame.time.get_ticks()
			if self.mostrar_texto_velocidad:
				self.ventana.blit(self.textoV, self.texto_rectV)
				if pygame.time.get_ticks() - self.tiempoi_tvelocidad > 500:
					self.mostrar_texto_velocidad = False
			if self.powerup2 and self.jugador_rect.colliderect(self.powerup2.rect):
				self.todoslossprites.remove(self.powerup2)
				self.powerup2 = None


			pygame.display.flip()
			self.__mostrarVidas()
			self.__mostrarPuntuacion()
			pygame.display.update()

	def __mostrarPuntuacion(self):
		self.fuenteP = pygame.font.SysFont('Consolas', 20)
		self.textoP = self.fuenteP.render(str(self.score).zfill(8), True, (0,0,0))
		self.textoRectP = self.textoP.get_rect()
		self.textoRectP.topleft = [0,0]
		ventana.blit(self.textoP, self.textoRectP)

	def __despausar(self):
		self.ventana = pygame.display.set_mode([ancho,alto])
		self.pausar = False

	def __pausa(self):
		self.ventana = pygame.display.set_mode(tamaño_del_menu)
		self.fuenteP = pygame.font.SysFont('Consolas', 72)
		self.textoFondo, self.textoRect = text_objects("Pausa", self.fuenteP)
		self.textoRect.center = ((ancho/2), (alto/2))
		self.ventana.blit(self.textoFondo, self.textoRect)
		
		while self.pausar:
			for self.evento in pygame.event.get():
				if self.evento.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			
			self.ventana.fill((255,255,255))
			
			boton("Despausar",120, 240, 100, 50, (200,0,0), (255,0,0), self.__despausar)
			boton("Salir",440, 240, 100, 50, (0,220,0), (0,255,0), game_menu.menu_del_juego)

			#boton("Despausar",150, 450, 100, 50, (200,0,0), (255,0,0), self.__despausar)
			#boton("Salir",550, 450, 100, 50, (0,220,0), (0,255,0), game_menu.menu_del_juego)
	
			pygame.display.update()
			clock.tick(15)

  

	def __mostrarVidas(self):
		self.fuenteP = pygame.font.SysFont('Consolas', 20)
		self.textoP = self.fuenteP.render(("Vidas:" + str(self.vidas)).zfill(2), True, (0,0,0))
		self.textoRectP = self.textoP.get_rect()
		self.textoRectP.topleft = [550,0]
		ventana.blit(self.textoP, self.textoRectP)

	def __tipochoque1(self):
		# En esta función se va a dar un powerup, en este caso un escudo al jugador cuando haya hecho collide
		self.efecto_choque1 = pygame.mixer.Sound("sonidos/punch_effect_1.wav")
		self.efecto_choque1.set_volume(1.0)
		self.efecto_choque1.play()        
	   

	def __tipochoque2(self):
		# En esta función se va a dar un powerup, en este caso un escudo al jugador cuando haya hecho collide
		self.efecto_choque2 = pygame.mixer.Sound("sonidos/punch_effect_2.wav")
		self.efecto_choque2.set_volume(0.7)
		self.efecto_choque2.play()        
	  

	def __heart(self):
		# En esta función se va a dar un powerup, en este caso un escudo al jugador cuando haya hecho collide
		self.efecto_powerup2 = pygame.mixer.Sound("sonidos/mariobros_life_effect.wav")
		self.efecto_powerup2.set_volume(0.5)
		self.efecto_powerup2.play()

		self.fuenteE = pygame.font.SysFont('Consolas', 30)
		self.textoE = self.fuenteE.render('Vida +1 ', True, (255,255,255))
		self.texto_rectE = self.textoE.get_rect()
		self.texto_rectE = [(ancho / 2) - 300, (alto-100) / 2]
		self.vidas = self.vidas + 1

	def __speed(self):
		# En esta función se va a dar un powerup, en este caso un rayo al jugador cuando haya hecho collide
		#pygame.mixer.Channel(1).play(pygame.mixer.Sound('falcon_punch.mp3'))
		self.efecto_powerup2 = pygame.mixer.Sound("sonidos/mariobros_mushroomeffect.wav")
		self.efecto_powerup2.set_volume(0.5)
		self.efecto_powerup2.play()

		self.fuenteV = pygame.font.SysFont('Consolas', 30)
		self.textoV = self.fuenteV.render('Speed++', True, (255,255,255))
		self.texto_rectV = self.textoV.get_rect()
		self.texto_rectV = [(ancho / 2) - 300, alto / 2]
		self.jugador.velocidad = 10

# Programación del Chusqui Runner
class Chasqui(pygame.sprite.Sprite):
	def __init__(self,posx,posy):
		pygame.sprite.Sprite.__init__(self)

		# Se va a hacer un cambio de todas las imagenes debido a que el chasqui va a tener que correr de forma dinámica, no estática
		if SKIN[0] == 'DEFAULT-EASY' or SKIN[0] == 'DEFAULT-MEDIUM' or SKIN[0] == 'DEFAULT-HARD':
			print("Inicializado sin cambios")
			self.imagen1 = pygame.image.load(r"CHASQUI00.png")
			self.imagen2 = pygame.image.load(r"CHASQUI01.png")
			self.imagen3 = pygame.image.load(r"CHASQUI02.png")
			self.imagen4 = pygame.image.load(r"CHASQUI03.png")
			self.imagen5 = pygame.image.load(r"CHASQUI04.png")
			self.imagen6 = pygame.image.load(r"CHASQUI05.png")
			self.imagen7 = pygame.image.load(r"CHASQUI06.png")
			self.imagen8 = pygame.image.load(r"CHASQUI07.png")      
			self.imagen9 = pygame.image.load(r"CHASQUI08.png")
			self.imagen10 = pygame.image.load(r"CHASQUI09.png")
			self.imagen11 = pygame.image.load(r"CHASQUI10.png")
			self.imagen12 = pygame.image.load(r"CHASQUI11.png")
			
			self.listaImagenes = [self.imagen1, self.imagen2, self.imagen3, self.imagen4,
					  self.imagen5, self.imagen6, self.imagen7, self.imagen8,
					  self.imagen9, self.imagen10, self.imagen11, self.imagen12]

		elif SKIN[0] == 'GOKU-EASY' or SKIN[0] == 'GOKU-MEDIUM' or SKIN[0] == 'GOKU-HARD':
			print("Inicializado con cambios {}".format(SKIN[0]))
			self.imagen1 = pygame.image.load(r"GOKU00.png")
			self.imagen2 = pygame.image.load(r"GOKU01.png")
			self.imagen3 = pygame.image.load(r"GOKU02.png")
			self.imagen4 = pygame.image.load(r"GOKU03.png")
			self.imagen5 = pygame.image.load(r"GOKU04.png")
			self.imagen6 = pygame.image.load(r"GOKU05.png")
			self.imagen7 = pygame.image.load(r"GOKU06.png")
			self.imagen8 = pygame.image.load(r"GOKU07.png")
			self.imagen9 = pygame.image.load(r"GOKU08.png")
			self.imagen10 = pygame.image.load(r"GOKU09.png")
			self.imagen11 = pygame.image.load(r"GOKU10.png")
			self.imagen12 = pygame.image.load(r"GOKU11.png")
			
			self.listaImagenes = [self.imagen1, self.imagen2, self.imagen3, self.imagen4,
					  self.imagen5, self.imagen6, self.imagen7, self.imagen8,
					  self.imagen9, self.imagen10, self.imagen11, self.imagen12]

		elif SKIN[0] == 'HULK-EASY' or SKIN[0] == 'HULK-MEDIUM' or SKIN[0] == 'HULK-HARD':
			print("Inicializado con cambios {}".format(SKIN[0]))
			self.imagen1 = pygame.image.load(r"HULK00.png")
			self.imagen2 = pygame.image.load(r"HULK01.png")
			self.imagen3 = pygame.image.load(r"HULK02.png")
			self.imagen4 = pygame.image.load(r"HULK03.png")
			self.imagen5 = pygame.image.load(r"HULK04.png")
			self.imagen6 = pygame.image.load(r"HULK05.png")
			self.imagen7 = pygame.image.load(r"HULK06.png")
			self.imagen8 = pygame.image.load(r"HULK07.png")
			self.imagen9 = pygame.image.load(r"HULK08.png")
			self.imagen10 = pygame.image.load(r"HULK09.png")
			self.imagen11 = pygame.image.load(r"HULK10.png")
			self.imagen12 = pygame.image.load(r"HULK11.png")
			
			self.listaImagenes = [self.imagen1, self.imagen2, self.imagen3, self.imagen4,
					  self.imagen5, self.imagen6, self.imagen7, self.imagen8,
					  self.imagen9, self.imagen10, self.imagen11, self.imagen12]
	  
		else:
			raise Exception('Unknown skin {0}'.format(SKIN))
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
							  self.imagen9, self.imagen10, self.imagen11, self.imagen12]
		self.posImagen = 0

		# Se pone la imagen encime del fondo
		self.imagenesPosicion = self.listaImagenes[self.posImagen]
		self.rect = self.imagenesPosicion.get_rect()

		# Sirve para recorrer la imagen de acuerdo al tiempo que se le otorque
		self.tiempoCambio = 1

		# Verificar si el jugador perdio
		self.partidaPerdida = False

		# La velocidad en la cual ira el chasqui
		self.velocidad = 6
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
		"""
		if SKIN[0] == 'DEFAULT-EASY' or SKIN[0] == 'DEFAULT-MEDIUM' or SKIN[0] == 'DEFAULT-HARD':
			pass
		elif SKIN[0] == 'GOKU-EASY' or SKIN[0] == 'GOKU-MEDIUM' or SKIN[0] == 'GOKU-HARD':
			pass
		elif SKIN[0] == 'HULK-EASY' or SKIN[0] == 'HULK-MEDIUM' or SKIN[0] == 'HULK-HARD':
			pass
		"""

		self.velocidad = 6
		self.rect.top = posy
		self.rect.left = posx
		self.scoreRec = 5

	def dibujar(self, superficie):
		superficie.blit(self.imagen, self.rect)

	def movimientoVertical(self):
		self.rect.top = self.rect.top + self.velocidad
		self.__repeticion()

	def __repeticion(self):
		if self.rect.top + 50 > alto:
			self.rect.top = -100

	def comportamiento(self, tiempito):
		if tiempito == self.scoreRec:
			self.velocidad = self.velocidad + 1
			self.scoreRec = self.scoreRec + 5


class Obstaculo2(pygame.sprite.Sprite):
	def __init__(self, posy, posx):
		pygame.sprite.Sprite.__init__(self)

		self.imagen = pygame.image.load("obstaculo2.png")
		self.rect = self.imagen.get_rect()

		self.validacion = 1

		self.velocidad = 4
		self.rect.top = posy
		self.rect.left = posx
		self.scoreRec = 5

	def dibujar(self, superficie):
		superficie.blit(self.imagen, self.rect)

	def movimientoVertical(self):
		self.rect.top = self.rect.top + self.velocidad
		self.__repeticion()

	def __repeticion(self):
		if self.rect.top + 50 > alto:
			self.rect.top = -100

	def comportamiento(self, tiempito):
		if tiempito == self.scoreRec:
			self.velocidad = self.velocidad + 1
			self.scoreRec = self.scoreRec + 5

class Obstaculo3(pygame.sprite.Sprite):
	def __init__(self, posy, posx):
		pygame.sprite.Sprite.__init__(self)

		self.imagen = pygame.image.load("obstaculo3.png")
		self.rect = self.imagen.get_rect()

		self.validacion = 1

		self.velocidad = 7
		self.rect.top = posy
		self.rect.left = posx
		self.scoreRec = 5

	def dibujar(self, superficie):
		superficie.blit(self.imagen, self.rect)

	def movimientoVertical(self):
		self.rect.top = self.rect.top + self.velocidad
		self.__repeticion()

	def __repeticion(self):
		if self.rect.top + 50 > alto:
			self.rect.top = -100

	def comportamiento(self, tiempito):
		if tiempito == self.scoreRec:
			self.velocidad = self.velocidad + 1
			self.scoreRec = self.scoreRec + 5

class PowerUp1(pygame.sprite.Sprite):
	def __init__(self, posy, posx):
		pygame.sprite.Sprite.__init__(self)

		self.imagen = pygame.image.load("pw1.png")
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
		if self.rect.top + 70 > alto:
			self.rect.top = -120

class PowerUp2(pygame.sprite.Sprite):
	def __init__(self, posy, posx):
		pygame.sprite.Sprite.__init__(self)

		self.imagen = pygame.image.load("pw2.png")
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
		if self.rect.top + 60 > alto:
			self.rect.top = -120

#    -----   MENU   -----
# MENU DEL JUEGO
class GameMenu():
	def menu_del_juego(self):		

		#MENU JUGAR
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

		self.menu_jugar.add_option('Empezar!', funcion_skin, SKIN)
		self.menu_jugar.add_selector('Escoger Skin', [('Default-Easy', 'DEFAULT-EASY'),
													 ('Goku-Easy', 'GOKU-EASY'),
													 ('Hulk-Easy', 'HULK-EASY'),

													 ('Default-Medium', 'DEFAULT-MEDIUM'),
													 ('Goku-Medium', 'GOKU-MEDIUM'),
													 ('Hulk-Medium', 'HULK-MEDIUM'),

													 ('Default-Hard', 'DEFAULT-HARD'),
													 ('Goku-Hard', 'GOKU-HARD'),
													 ('Hulk-Hard', 'HULK-HARD'),],
								onreturn = False,
								onchange = cambiar_skin)
		self.menu_jugar.add_option('REGRESAR AL MENU PRINCIPAL', PYGAME_MENU_BACK)

		

		# MENU SOBRE NOSOTROS
		self.menu_sobre_nosotros = pygameMenu.TextMenu(ventana,
												bgfun=background,
												color_selected=color_negro,
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

		# Opciones del Menú Configurador
		# Opción 1: Seleccionar Skins
		# Opción 2: Elegir fondo del juego
		# Opción 3: Cambiar la dificultad
		# Opción 4: Configurar obstáculos y powerups

		# MENÚ EDICIÓN SKINS
		self.menu_eskins = pygameMenu.Menu(ventana,
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
										title='Editar Skins',
										window_height=tamaño_del_menu[1],
										window_width=tamaño_del_menu[0]
										)
		self.menu_eskins.add_option('Empezar juego', game.ChasquiRunner)
		self.menu_eskins.add_option('Buscar skin', tkinbuscar)
		self.menu_eskins.add_option('REGRESAR AL MENU PRINCIPAL', PYGAME_MENU_BACK)


		# MENÚ SELECCIÓN FONDO
		self.menu_efondo = pygameMenu.Menu(ventana,
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
										title='Seleccionar Fondo',
										window_height=tamaño_del_menu[1],
										window_width=tamaño_del_menu[0]
										)
		self.menu_efondo.add_option('Empezar Juego', game.ChasquiRunner)
		self.menu_efondo.add_option('Buscar skin', tkinbuscar)
		self.menu_efondo.add_option('REGRESAR AL MENU PRINCIPAL', PYGAME_MENU_BACK)

		# MENÚ CONFIGURACIÓN DE DIFICULTAD
		self.menu_edifi = pygameMenu.Menu(ventana,
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
										title='Cambiar dificultad',
										window_height=tamaño_del_menu[1],
										window_width=tamaño_del_menu[0]
										)
		self.menu_edifi.add_option('Empezar Juego', game.ChasquiRunner)
		self.menu_edifi.add_option('Buscar skin', tkinbuscar)
		self.menu_edifi.add_option('REGRESAR AL MENU PRINCIPAL', PYGAME_MENU_BACK)

		# MENÚ CONFIGURACIÓN DE OBSTÁCULOS Y POWERUPS
		self.menu_obspw = pygameMenu.Menu(ventana,
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
										title='Configurar obstaculos y powerups',
										window_height=tamaño_del_menu[1],
										window_width=tamaño_del_menu[0]
										)
		self.menu_obspw.add_option('Empezar!', game.ChasquiRunner)
		self.menu_obspw.add_option('Buscar skin', tkinbuscar)
		self.menu_obspw.add_option('REGRESAR AL MENU PRINCIPAL', PYGAME_MENU_BACK)


		# MENU CONFIGURADOR
		self.menu_configurador = pygameMenu.TextMenu(ventana,
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
										title='Menu Configurador',
										window_height=tamaño_del_menu[1],
										window_width=tamaño_del_menu[0]
										)

		self.menu_configurador.add_option('Editar skins', self.menu_eskins)
		self.menu_configurador.add_option('Editar fondo', self.menu_efondo)
		self.menu_configurador.add_option('Cambiar dificultad', self.menu_edifi)
		self.menu_configurador.add_option('Configurar obstaculos y powerups', self.menu_obspw)
		self.menu_configurador.add_option('Regresar al menu principal', PYGAME_MENU_BACK)

		# MENU PRINCIPAL
		self.menu_principal = pygameMenu.TextMenu(ventana,
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
		self.menu_principal.add_option('Configuracion de Objetos', self.menu_configurador)
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
#Centrar la ventana del juego
os.environ['SDL_VIDEO_CENTERED'] = '1'
#asignar tamaño inicial de la ventana
ventana = pygame.display.set_mode(tamaño_del_menu)
pygame.display.set_caption("CHASQUI RUNNER MENU")
clock = pygame.time.Clock()

# Comenzamos a llamar a la clase GameMenu para inicializar el Menú del juego
game_menu = GameMenu()
game_menu.menu_del_juego()