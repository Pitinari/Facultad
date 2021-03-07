
# En esta implementación del juego, se tomaron ciertas decisiones sobre las estructuras de datos a usar y el diseño. Se hace
# entonces una descripción general de los puntos más relevantes.
#
# * La palabra a adivinar es seleccionada en forma aleatoria de una lista predefinida de palabras posibles ('palabras').
#
# * La palabra a adivinar es guardada internamente como un String ('palabraOculta'). 
#
# * La palabra que se va completando a medida que el jugador va sugiriendo letras, es representada como 
#   una lista de char ('incognita'), de igual longitud que la palabra a adivinar. Esta lista es iniciada con un '_' por cada letra 
#   de esta última. A medida que se van sugiriendo letras que están en la palabra a adivinar, los '_' son sustituidos 
#	por dichas letras.
#
# * El programa guarda las letras que va sugiriendo el jugador en una lista ('letrasUsadas'). Así, utilizando esta lista, 
#   cuando el jugador ingresa una nueva letra, el programa verificará que se trate de una letra del abecedario que no haya sido 
#   ya propuesta. En el caso en que lo ingresado no sea una letra o sea una letra repetida, el programa dará un mensaje de error 
#   pero no descontará una vida.
#
# * Cuando el jugador ingresa una letra no repetida, ésta será buscada en la palabra a adivinar ('palabraOculta'), 
#   recorriendo esta última y guardando, en una lista ('listaIndices'), enteros que identifican las posiciones (si las hay) 
#   en la cuales dicha letra aparece en la palabra. 
#   Si esta lista es vacía, la letra no está en la palabra y el jugador perderá una vida. Si hay elementos, el programa 
#   ubicará la letra en la palabra oculta ('palabraOculta'); sustituyendo el '_' por la letra  
#   en las posiciones indicadas por la lista de enteros mencionada ('listaIndices').
#
# * Para controlar los posibles errores en los ingresos de los jugadores, cuando se espera una letra, el programa transforma el
#	caracter ingresado a Unicode (usando 'ord') y establece si el código obtenido corresponde al código de una de las letras 
#	del abecesario. En el caso en que el jugador ingrese más de un caracter (no es posible usar 'ord'), el programa manejará 
#	la excepción (usando try).


from random import *

#--------------------------------------------------
# inicializarIncognita: String -> [Char]
# Descripción: esta función recibe la palabra a adivinar y devuelve la una secuencia de guiones representando dicha palabra.

def inicializarIncognita(palabra):
	longitudPalabra = len(palabra)
	return ['_'] * longitudPalabra
#--------------------------------------------------
#obtenerPalabraOculta: None -> String
#Descripción: esta función selecciona una palabra, de una lista predefinida de éstas, y la devuelve como resultado.

def obtenerPalabraOculta():
	palabras=['hola', 'puma', 'pizza','casa'] 	#Define la lista de posibles palabras ocultas.
	cantidadPalabras = len(palabras)			#Calcula la cantidad de posibles palabras ocultas.
	posicion = randrange(cantidadPalabras)		#Elige aleatoriamente una posición de la lista de palabras posibles.
	return palabras[posicion]					#Devuelve la palabra que está en la posición elegida.

#--------------------------------------------------
# esLetra1 y esLetra2 son dos opciones para definir una función que controle que el caracter ingresado por el usuario es una letra.

# esLetra1: Char -> Boolean
# Descripción: esta función recibe un caracter, lo transforma en código Unicode y evalúa si dicho código
# corresponde a una letra del abecedario. En caso afirmativo, devolverá True; en caso contrario, False.

def esLetra1(letra):
	try:
		orden=ord(letra)		#Transforma un caracter en su correspondiente código Unicode.
	except TypeError:
		print("Excepción en esLetra1: No es un caracter.")  #Si el elemento ingresado no es un caracter, captura la excepción.
		return False
	
	if (orden >= 65 and orden <= 90) or (orden >= 97 and orden <= 122) or orden==209 or orden==241: #Determina si el código 
		return True																					#corresponde a un caracter.
	else:
		return False
		
		
		
#Otra opción
# esLetra2: Char -> Boolean
# Descripción: esta función recibe un caracter y evalúa si éste está en una cadena formada por todas las letras 
# del abecedario, en mayúscula y minúscula. En caso afirmativo, devolverá True; en caso contrario, False.

def esLetra2(letra):
	abc='abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
	try:
		return letra in abc
	except TypeError:
		print("Excepción en esLetra2: No es un caracter.")
		return False
#--------------------------------------------------
		
# pedirLetra: [Char] Char -> Char
# Descripción: esta función recibe la lista de letras ya ingresadas por el usuario y 
# el caracter identificador de interrupción del juego. Entonces, solicita al usuario que ingrese una letra o bien 
# el caracter de interrupción del juego, si quiere dejar de jugar. Si el usuario eligió dejar de jugar, devolverá el
# caracter de interrupción. Si ingresó una letra que no había sido ingresada antes, la agregará 
# a la lista de letras usadas y la dará como resultado. Si ya fue usada o no es una letra, devolverá un caracter vacío.

def pedirLetra(letrasUsadas, bandera):
	letra=input('Ingrese por favor una letra o '+ bandera+ ' para terminar: ')
	if letra == bandera:				#Determina si el valor ingresado por el usuario es el caracter de interrupción del juego
		return bandera
	else:
		letra=letra.lower()
		if esLetra1(letra) and letra not in letrasUsadas:	#Determina si el caracter ingresado por el usuario es una letra válida
			letrasUsadas+=[letra]
			return letra
		else:
			return ''


#-----------------------------------------------

# buscarPosiciones: Char Sting -> [Int]
# Descripción: esta función recibe una letra y una palabra; y devuelve la lista de posiciones en la palabra, en las cuales aparece 
# la letra ingresada.
def buscarPosiciones(letra, palabra):
	longitudPalabra = len(palabra)		#Determina la longitud de la palabra.
	indices = []
	for i in range(longitudPalabra):	#Recorre la palabra y guarda las posiciones (en 'indices') en las cuales la letra aparece.
		if letra == palabra[i]:
			indices+=[i]
	return indices						#Devuelve la lista de posiciones.
		
#--------------------------------------------------

# palabraIncompleta: [Char] -> Bool
# Descripción: esta función devuelve la palabra a completar (lista de '_') y establece si ha sido completada o no.
def palabraIncompleta(palabraLista):
	simbolo='_'
	return simbolo in palabraLista		# Si hay '_' en la lista, la palabra todavía no fue completada.
#--------------------------------------------------

# completarLetra: [Char] [Int] Char -> None
# Descripción: esta función recibe la palabra a completar (incognita), la lista de posiciones donde aparece cierta letra (listaIndices) 
# y dicha letra. Así, ubica la letra ingresada, en la palabra a completar, en las posiciones indicadas en la lista.

def completarLetra(incognita, listaIndices, letra):
	for i in listaIndices:
		incognita[i]=letra
		
#--------------------------------------------------

# mostrarIncognita: [Char] -> None
# Descripción: esta función recibe una la palabra a descubrir que se fue completando y la muestra.

def mostrarIncognita(incognita):
	print('\n')
	for i in incognita:
		print(i, end=' ')
	print('\n')

#--------------------------------------------------	

# jugar: None -> None
# Descripción: esta es la función principal, la cual inicia y lleva adelante el juego hasta el final.

def jugar():
	bandera='1'		# 'bandera' guarda el caracter identificador de interrupción de la jugada.
	vidas=6			# 'vidas' guarda la cantidad de vidas que tiene el jugador para adivinar la palabra.
	fin=False		# 'fin' se utiliza para establecer si el juego debe ser interrumpido.
	letrasUsadas=[]		# Guarda la lista de letras ya ingresadas por el jugador.	
	listaIndices=[]		# Guardar las posiciones en las que aparece una letra, ingresada por el jugador, en la palabra oculta.
	palabraOculta = obtenerPalabraOculta() 		# Obtiener aleatoriamente una palabra oculta para adivinar. 
												# (palabraOculta: String).
	incognita = inicializarIncognita(palabraOculta) # Generar la secuencia de guiones que representa la palabra oculta 
													# (incognita: [Char])
	mostrarIncognita(incognita)	# Muestra la palabra a completar (secuencia de guiones).
	print('Bienvenides al juego \'El Ahorcado\'\n')
	
	while palabraIncompleta(incognita) and vidas > 0 and not fin: 	# Mientras la incognita no haya sido completada, 
																	# haya vidas disponibles y no se haya interrumpido el juego,
																	# seguir jugando.
		print('Puede equivocarse a lo sumo ', vidas-1, 'veces.\n')
		letra = pedirLetra(letrasUsadas, bandera)		# Solicitar al jugador que ingrese la letra sugerida.
		if letra == bandera:		# Si la letra sugerida es el identificador de interrupción del juego, terminar el juego.
			fin=True
		elif letra=='': 	# Si no, pregunta si lo ingresado por el jugador no fue una letra válida.
			print('El caracter ingresado no es una letra o es una letra que ya fue utilizada.\n')
		else:
			listaIndices = buscarPosiciones(letra, palabraOculta)	# Si lo ingresado fue una letra válida; busca las posiciones en 
																	# la palabra oculta, en las que pudiera aparecer la dicha letra.
			if listaIndices==[]:	# Si la letra no aparece en ninguna posición de la palabra oculta, se restará una vida.
				vidas-=1
				print('Usted ha perdido una vida.\n')
			else:					# Si la letra aparece en la palabra oculta, 
				completarLetra(incognita,listaIndices,letra) # se completará en esta última con la letra
				mostrarIncognita(incognita)		# y se la mostrará.
	
	# Al salir del bucle, se pregunta la causa de la salida, para dar diferentes mensajes al jugador.			
	if vidas == 0: 	# Se le acabaron las vidas y, por tanto, el jugador perdió.
		print('Usted ha perdido.\n')
		print('La palabra oculta es:', palabraOculta)
	elif fin: # El jugador interrumpió el juego.
		print('Usted ha interrupido el juego.')
	else:	# El jugador ganó.
		print('¡Felicitaciones! Usted ha ganado. ')

#--------------------------------------------------		
#Iniciar el juego.
jugar()
