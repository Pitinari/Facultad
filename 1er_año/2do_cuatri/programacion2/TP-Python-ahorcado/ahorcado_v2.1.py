# En esta implementación del juego, se tomaron ciertas decisiones sobre las estructuras de datos a usar y el diseño. Se hace
# entonces una descripción general de los puntos más relevantes.
#
# * La palabra a adivinar es solicitada por el programa, a un jugador que la ingresará por teclado. El programa verificará que las 
#   letras de dicha palabra pertenezca al abededario.
#
# * La palabra a adivinar es guardada internamente como un String ('palabraSecreta').
#
# * La palabra que se va completando a medida que el jugador va sugiriendo letras, es representada como 
#   un String ('palabraAdivinada'), de igual longitud que la palabra a adivinar. Este String es inicialmente una secuencia de 
#   '-', uno por cada letra de la palabra a adivinar. A medida que se van sugiriendo letras que están en la palabra a adivinar, 
#   los '-' son sustituidos por dichas letras.
#	
# * El programa guarda en un String ('letrasYaJugadas'), las letras que va sugiriendo el jugador. Así, utilizando este String, 
#   cuando el jugador ingresa una nueva letra, el programa verificará que se trate de una letra del abecedario que no haya sido 
#   ya sugerida. En el caso en que lo ingresado no sea una letra o sea una letra repetida, el programa dará un mensaje de error 
#   pero no descontará una vida, simplemente volverá a solicitar una nueva letra.
#
# * Cuando el jugador ingresa una letra que está en el abecedario y no está repetida, el programa evalúa si la letra es un substring
#   de la palabra a adivinar ('palabraSecreta'). Si no lo es, descontará una vida. Si lo es, recorrerá la palabra a adivinar
#   para determinar en qué posiciones está la letra. Cuando la encuentra en una cierta posición, sustituye en 
#   la palabra oculta ('palabraAdivinada') el '-' por dicha letra.
#
# * Para controlar los posibles errores en los ingresos de los jugadores, el programa verifica que cuando se espera una letra, 
#	la cadena ingresada tenga longitud 1 y sea un substring del abecedario. Y en el caso de que lo esperado sea una palabra, 
#	el programa verifica que cada caracter de la cadena sea un substring del abecedario.
#


#--------------------------------------------------
# Función reutilizada de "Ahorcado_v2.1"
# inicializarAlfabeto: None -> String
# Descripción: Devuelve el alfabeto con el que se va a jugar.

def inicializarAlfabeto():
    return 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    
    
#--------------------------------------------------
# Función reutilizada de "Ahorcado_v2.1"
# inicializarPalabraAdivinada: Int -> String
# Descripción: recibe la longitud de la palabra a adivinar y devuele un String de '-' consecutivos, 
# de la misma longitud que la palabra.

def inicializarPalabraAdivinada(tamanio):
    return '-' * tamanio


#--------------------------------------------------
# chequearPalabra: String String -> Bool
# Descripción: esta función recibe una palabra y un abecesario, y determina si todos las letras de la palabra pertenecen
# al abecedario. Para esto recorre la palabra letra por letra determinando si éstas están en el abecedario.

def chequearPalabra(palabra,alfabeto):
    posicion = 0
    cantidadLetras = len(palabra)
    while posicion < cantidadLetras  and palabra[posicion] in alfabeto:
        posicion += 1
    return (posicion == cantidadLetras)

#--------------------------------------------------
# ingresarPalabra: String -> String
# Descripción: esta función recibe el alfabeto que se va a utilizar y solicita al jugador que ingrese la palabra a adivinar. Usando
# el alfabeto, determinará si la palabra ingresada está construida con dicho alfabeto y es una palabra válida. En caso de no serlo, 
# dará un mensaje de error y seguirá solicitando una palabra hasta que la ingresada sea válida. Cuando esto ocurra, devolverá la
# palabra válida en mayúscula, independientemente de cómo haya sido ingresada.

def ingresarPalabra(alfabeto):
    palabra = input('Jugador 1, por favor, ingrese la palabra secreta\n')
    palabra = palabra.upper()
    while(not chequearPalabra(palabra,alfabeto)):	# Mientras la palabra no sea válida, pedir una palabra a adivinar.
        print('ERROR - La palabra ingresada contiene caracteres no validos')
        palabra = input('Jugador 1, por favor, ingrese la palabra secreta')
        palabra = palabra.upper()
    return palabra



#--------------------------------------------------
# chequearLetra: String String String -> Bool
# Descripción: esta función verifica que una cadena sea una letra, que esté en el abcedario y no haya sido previamente ingresada. 
# Si no es un caracter, no está en el alfabeto o ya fue ingresada, dará un mensaje de error y devolverá False. En caso contrario, 
# devolverá True.

def chequearLetra(letra,alfabeto,yaJugadas):
    chequeo = True
    if (len(letra)>1):	# Si no es un caracter, dará un error.
        print('Error - Ingreso mas de un caracter')
        chequeo = False
    elif (letra not in alfabeto): # Si es un caracter pero no está en el abecedario, dará un error.
        print('Error - Ingreso un caracter invalido')
        chequeo = False
    elif (letra in yaJugadas): # Si es un caracter que está en el abecedario y pero ya fue ingresado, dará un error.
        print('Error - Letra ya jugada')
        chequeo = False
    return chequeo # Si nada de lo anterior se cumple, es un caracter válido y devuelve True.
    

#--------------------------------------------------
# ingresarLetra: String String -> Char
# Descripción: esta función recibe un alfabeto y las letras ya ingresadas por el jugador, y solicita a éste que ingrese una 
# nueva letra sugerida. Mientras el jugador no ingrese una letra que esté en el alfabeto y no haya sido ingresada previamente,
# la función seguirá pidiendo el ingreso de una nueva letra. Cuando la letra ingresada sea válida, la función la devolverá 
# en mayúscula, independientemente de cómo la haya ingresado el jugador.

def ingresarLetra(alfabeto,letrasYaJugadas):
    letra = input('Ingrese una letra: ')
    letra = letra.upper()
    while(not chequearLetra(letra,alfabeto,letrasYaJugadas)): # Mientras no sea una letra válida, pedir una letra.
        letra=input('Vuelva a ingresar una letra: ')
        letra=letra.upper()
    return letra
    

#--------------------------------------------------
# jugar: None -> None
# Descripción: esta es la función principal, la cual inicia y lleva adelante el juego hasta el final.

def jugar():
    print('Bienvenido al juego del Ahorcado')
    alfabeto = inicializarAlfabeto()	# Obtiener el alfabeto que se va a utilizar (alfabeto:String).
    letrasYaJugadas = ''				# Guardar las letras propuestas por el jugador.
    gano = False						# Identificador de si el jugador ha ganado o no.
    vidas = 6							# 'vidas' guarda la cantidad de vidas que tiene el jugador para adivinar la palabra.
    
    palabraSecreta = ingresarPalabra(alfabeto)	# Solicitar que se ingrese la palabra a adivinar (palabraSecreta:String).
    
    palabraAdivinada = inicializarPalabraAdivinada(len(palabraSecreta)) # Generar la secuencia de '-' que representa la palabra oculta (palabraAdivinada: String)
    print('Jugador 2, es hora de adivinar!')
    while(vidas > 0 and not palabraSecreta==palabraAdivinada):	# Mientras haya vidas y la palabra oculta sea diferente de la 
																# palabra a adivinar, seguir jugando.
        print('Juegue: ')
        print('Palabra Secreta:\n', palabraAdivinada)			# Mostrar la palabra oculta.
        letra = ingresarLetra(alfabeto,letrasYaJugadas)			# Solicitar al jugador que ingrese una letra.
        letrasYaJugadas=letrasYaJugadas+letra					# Guardar la letra ingresada.
        if(letra not in palabraSecreta):						# Si la letra no está en la palabra a adivinar, se restará una vida.
            vidas -=1
        else:											# Si la letra está en la palabra a adivinar,
            for x in range(0,len(palabraSecreta)):		# recorrer esta última para saber en qué posiciones la letra aparece.
                if(palabraSecreta[x]==letra):			# En dichar posiciones, sustituye '-' en la palabra oculta por la letra.
                    palabraAdivinada= palabraAdivinada[:x]+letra+palabraAdivinada[x+1:]
                    
	# Al salir del bucle, se pregunta la causa de la salida, para dar diferentes mensajes al jugador.	                    
    if(palabraSecreta==palabraAdivinada):	# La palabra fue adivinada. El jugador ganó.
        print('Felicitaciones! Adivino la palabra secreta: ', palabraSecreta)
    else:			# Se acabaron las vidas. El jugador perdió.
        print('Ud. ha perdido - La palabra secreta era: ', palabraSecreta)
            

#--------------------------------------------------	
#Iniciar el juego.
jugar()
