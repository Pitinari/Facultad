#####################################
#   TRABAJO PRACTICO PYTHON         #
#         INTEGRANTES:              #
# PITINARI, TOMAS ; QUINTERO, IAGO  #
#####################################


import sys
import os.path
import random

#recibe path para el archivo, retorna diccionario con jugadores y sus jugadas
# estructura {nombre: (palabra, gano, intentos) , ...}
#cargarDatosJugadores: string -> {string:(string, bool, int)}
def cargarDatosJugadores(datosJugadoresPath):
    
    if not os.path.isfile(datosJugadoresPath): 
        #handleo archivo no existe, retorno diccionario vacio
        return {}

    #abrir el archivo y que se cierre automaticamente
    with open(datosJugadoresPath) as archivo:
        #iteramos sobre todas las lineas

        datosJugadores = {}
        nombreJugadorActual = ''
        jugadasJugadorActual = []
        for linea in archivo.readlines():
            #separamos la linea en sus valores separados por coma, eliminamos espacios
            valoresLinea = linea.replace(" ", "").split(",")
            if len(valoresLinea) == 1:
                #un solo valor en la linea, por lo tanto es un nuevo jugador
                
                nombreJugadorActual = valoresLinea[0].rstrip()
                jugadasJugadorActual = [] if not nombreJugadorActual in datosJugadores else datosJugadores[nombreJugadorActual]
                
                #guardamos jugador en la estructura, (si existe)
                if nombreJugadorActual != '' and nombreJugadorActual != '\n':
                    datosJugadores[nombreJugadorActual] = jugadasJugadorActual
                
            if len(valoresLinea) == 3:
                # tres valores, por lo tanto es registro de un juego
                palabra = valoresLinea[0]
                gano = valoresLinea[1]
                intentos = int(valoresLinea[2])

                #guardamos el juego para el jugador
                jugadasJugadorActual.append((palabra,gano,intentos))
        
        #retorna estructura generada
        return datosJugadores


# Representamos la jugada como una tupla de 2 strings y un int
# generarLinea: (string, string, int) -> string
# Recibe una jugada y retorna la linea para escribir en el archivo
#Entrada: ("quiero", "NO", 4) Salida 
#Entrada: ("mas", "SI", 6)
#Entrada:  ("mesas", "NO", 4)
def generarLinea(jugada):
    (palabra, gano, intentos) = jugada
    #escribir sus jugadas
    return palabra + ', ' + gano + ', ' + str(intentos) + '\n'

def test_generarLinea():
    assert generarLinea(("quiero", "NO", 4)) == "quiero, NO, 4\n"
    assert generarLinea(("mas", "SI", 6)) == "mas, SI, 6\n"
    assert generarLinea(("mesas", "NO", 4)) == "mesas, NO, 4\n"


#-------------------------------------------------------------------
#Representamos los datos de los jugadores, donde los datos son un diccionario 
#donde los jugadores son las claves de cada dato y la ruta del archivo de jugadores
#como un string
#guardarDatosJugadores: {string:(string, bool, int)} string -> None
#sobreescribe el archivo de jugadores con la información anterior y la nueva
def guardarDatosJugadores(datosJugadores, datosJugadoresPath):
    #abrir archivo, o crearlo
    with open(datosJugadoresPath, 'w') as archivo:
        #iteramos por cada jugador en el diccionario
        for (jugador, jugadas) in datosJugadores.items():
            #escribir nombre del jugdor
            archivo.write(jugador + '\n')
            for (palabra, gano, intentos) in jugadas:
                #escribir sus jugadas
                linea = palabra + ', ' + gano + ', ' + str(intentos) + '\n'
                archivo.write(linea)


#--------------------------------------
#Representamos la ruta del lemario como un string
# y todas las palabras del archivo como un conjunto de strings
#cargarLemario: string -> set(string)
#la función va a abrir el archivo y va a guardar linea por linea en un conjunto
def cargarLemario(lemarioPath):
    
    #abrir el archivo y que se cierre automaticamente
    with open(lemarioPath) as archivo:
        palabras = set()
        #guardar cada palabra en un conjunto
        for linea in archivo.readlines():
            palabras.add(linea.strip())
        return palabras


#----------------------------------------------------------
#Representamos las palabras usadas y del lemario como conjuntos de strings
# y retornamos una palabra como un string
#elegirPalabraNoRepetida: set(string) set(string) -> string
#Dadas las palabras usadas y las palabras totales nuestra funcion va a devolver
# una palabra aleatoria de las palabras no usadas
#Entrada: set("casa") set("la","casa","linda") Salida: palabra in {"la","linda"}
#Entrada: set("la") set("la","casa","linda") Salida: palabra in {"casa","linda"}
def elegirPalabraNoRepetida(palabrasUsadas, lemario):

    #calcular las palabras no usadas
    palabrasNoUsadas = lemario - palabrasUsadas
    #devuelve string vacio si se usaron todas las palabras
    if len(palabrasNoUsadas) == 0:
        return ''
    
    palabra = random.sample(palabrasNoUsadas,1)[0].upper()
    while(not chequearPalabra(palabra,inicializarAlfabeto())):	# Mientras la palabra no sea válida, pedir una palabra a adivinar.
        palabra = random.sample(palabrasNoUsadas,1)[0].upper()
    #retornar palabra aleatoria de las no usadas
    return palabra

def test_elegirPalabraNoRepetida():
    assert (elegirPalabraNoRepetida({'hola','profes'}, {'hola','profes','palabras','extra'}) in {'PALABRAS', 'EXTRA'})
    assert elegirPalabraNoRepetida({'hola','profes'}, {'hola','profes'}) == ''

#-------------------------------------------------------------------------------------------------------------
#Representamos al jugador como un string y sus datos como un diccionario 
#donde los jugadores son las claves. Luego se devuelven las palabras como un conjunto
#palabrasJugador: string {string:(string, bool, int)} -> set(string)
#Dado un jugador queremos que nos devuelva todas la palabras que ya jugó
#Entrada: "Tomas" {"Tomas":[("hola",SI,6),("chau",NO,8)], "Iago":[("chau",SI,5)]} Salida: set("hola","chau")
#Entrada: "Tomas" {"Tomas":[], "Iago":[("chau",NO,5)]} Salida: set()

def palabrasJugador(jugador, datosJugadores):
    #obtener los juegos del jugador
    juegos = datosJugadores[jugador]
    
    palabras = set()
    #agregar la palabra de cada juego en un set y retornarlo
    for (palabra, gano, intentos) in juegos:
        palabras.add(palabra)

    return palabras

def test_palabrasJugador():
    assert palabrasJugador("Tomas",{"Tomas":[("hola",'SI',6),("chau",'NO',8)], "Iago":[("chau",'SI',5)]}) == {"hola","chau"}
    assert palabrasJugador("Tomas",{"Tomas":[], "Iago":[("chau",'SI',5)]}) == set()
    
#--------------------------------------------------
# Función reutilizada de "Ahorcado_v2.1"
# inicializarAlfabeto: None -> String
# Descripción: Devuelve el alfabeto con el que se va a jugar.

def inicializarAlfabeto():
    return 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    
def test_inicializarAlfabeto():
    assert inicializarAlfabeto() == 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

#--------------------------------------------------
# Función reutilizada de "Ahorcado_v2.1"
# inicializarPalabraAdivinada: Int -> String
# Descripción: recibe la longitud de la palabra a adivinar y devuele un String de '-' consecutivos, 
# de la misma longitud que la palabra.

def inicializarPalabraAdivinada(tamanio):
    return '-' * tamanio

def test_inicializarPalabraAdivinada():
    assert inicializarPalabraAdivinada(4) == '----'
    assert inicializarPalabraAdivinada(0) == ''
    assert inicializarPalabraAdivinada(8) == '--------'
    assert inicializarPalabraAdivinada(3) == '---'

#--------------------------------------------------
# Función reutilizada de "Ahorcado_v2.1"
# chequearPalabra: String String -> Bool
# Descripción: esta función recibe una palabra y un abecesario, y determina si todos las letras de la palabra pertenecen
# al abecedario. Para esto recorre la palabra letra por letra determinando si éstas están en el abecedario.

def chequearPalabra(palabra,alfabeto):
    posicion = 0
    cantidadLetras = len(palabra)
    while posicion < cantidadLetras  and palabra[posicion] in alfabeto:
        posicion += 1
    return (posicion == cantidadLetras)
    
def test_chequearPalabra():
    alfabeto = inicializarAlfabeto()
    assert chequearPalabra("CUANDO", alfabeto) == True
    assert chequearPalabra("r3nd1m0s", alfabeto) == False
    assert chequearPalabra("ALGEBRA", alfabeto) == True
    assert chequearPalabra("por favor", alfabeto) == False

#--------------------------------------------------
# Función reutilizada de "Ahorcado_v2.1"
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
    
def test_chequearLetra():
    alfabeto = inicializarAlfabeto()
    assert chequearLetra('A',alfabeto, 'BFD') == True
    assert chequearLetra('3',alfabeto, 'ELKDE') == False
    assert chequearLetra('S',alfabeto, 'SJDIDKE') == False

#--------------------------------------------------
# Función reutilizada de "Ahorcado_v2.1"
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
  
#---------------------------------------------------
#Muestra con una horca en ASCII el progreso en vidas
#mostrarHorca : Int -> String
#Representa una horca como un string en base de las vidas que tiene el jugador
def mostrarHorca(vidas):
    if vidas == 6:
        print("   |------|\n   |\n   |\n   |\n   |\n|-----|")
    elif vidas == 5:
        print("   |------|\n   |      O\n   |\n   |\n   |\n|-----|")
    elif vidas == 4:
        print("   |------|\n   |      O\n   |      |\n   |\n   |\n|-----|")
    elif vidas == 3:
        print("   |------|\n   |      O\n   |     /|\n   |\n   |\n|-----|")
    elif vidas == 2:
        print("   |------|\n   |      O\n   |     /|\ \n   |\n   |\n|-----|")
    elif vidas == 1:
        print("   |------|\n   |      O\n   |     /|\ \n   |     / \n   |\n|-----|")
    

#Función principal para jugar
def inicioPrograma():

    lemarioPath = ''
    datosJugadoresPath = ''

    #recuperar caminos para archivos
    argumentos = sys.argv
    if len(argumentos) >= 3:
        lemarioPath = argumentos[1]
        datosJugadoresPath = argumentos[2]

    #Si no existen las rutas de los archivos pide una valida
    while not os.path.isfile(lemarioPath):
        lemarioPath = input("Ingrese una ruta valida para el lemario: ")
        
    while not os.path.isfile(datosJugadoresPath):
        datosJugadoresPath = input("Ingrese una ruta valida para los jugadores: ")

    
    # cargar lemario, si esta vacio no se puede jugar
    lemario = cargarLemario(lemarioPath)
    if lemario == set():
        print("el lemario esta vacio, no se puede jugar")
        return 0
    
    # cargar datos jugadores
    datosJugadores = cargarDatosJugadores(datosJugadoresPath)

    # solicitar nombre de jugador
    jugador = input("Ingrese el nombre del jugador: ")
    
    #checkear si existe, si no existe agregarlo al diccionario de jugadores
    if not jugador in datosJugadores:
        datosJugadores[jugador] = []

    # elegir palabra aleatoria del lemario
    palabra = elegirPalabraNoRepetida(palabrasJugador(jugador, datosJugadores), lemario)
    
    # jugar juego
    print('Bienvenido al juego del Ahorcado')
    letrasYaJugadas = ''				# Guardar las letras propuestas por el jugador.
    vidas = 6							# 'vidas' guarda la cantidad de vidas que tiene el jugador para adivinar la palabra.
    gano= False
    palabraAdivinada = inicializarPalabraAdivinada(len(palabra)) # Generar la secuencia de '-' que representa la palabra oculta (palabraAdivinada: String)
    print(jugador + ', es hora de adivinar!')
    while(vidas > 0 and not palabra==palabraAdivinada):	# Mientras haya vidas y la palabra oculta sea diferente de la palabra a adivinar, seguir jugando.
        print('Palabra Secreta:\n', palabraAdivinada)			# Mostrar la palabra oculta.
        mostrarHorca(vidas)
        msgLetras= 'Ud. uso las letras: '
        for i in letrasYaJugadas:
            msgLetras += i + ", "
        msgLetras = msgLetras[0:len(msgLetras)-2]
        print(msgLetras)
        letra = ingresarLetra(inicializarAlfabeto(),letrasYaJugadas)			# Solicitar al jugador que ingrese una letra.
        letrasYaJugadas=letrasYaJugadas+letra					# Guardar la letra ingresada.
        if(letra not in palabra):						# Si la letra no está en la palabra a adivinar, se restará una vida.
            vidas -=1
        else:											# Si la letra está en la palabra a adivinar,
            for x in range(0,len(palabra)):		# recorrer esta última para saber en qué posiciones la letra aparece.
                if(palabra[x]==letra):			# En dichar posiciones, sustituye '-' en la palabra oculta por la letra.
                    palabraAdivinada= palabraAdivinada[:x]+letra+palabraAdivinada[x+1:]
                    
    # Al salir del bucle, se pregunta la causa de la salida, para dar diferentes mensajes al jugador.	                    
    if(palabra==palabraAdivinada):	# La palabra fue adivinada. El jugador ganó.
        print('Felicitaciones! Adivino la palabra secreta: ', palabra)
        gano = True
    else:			# Se acabaron las vidas. El jugador perdió.
        print('Ud. ha perdido - La palabra secreta era: ', palabra)
        print("   |------|\n   |      O\n   |     /|\ \n   |     / \ \n   |\n|-----|")

    # almacenar datos del juego al diccionario de jugadores
    datosJugadores[jugador].append((palabra,'SI' if gano else 'NO',len(letrasYaJugadas)))
    #reescribir archivo de jugadores
    guardarDatosJugadores(datosJugadores, datosJugadoresPath)
 
#Si corremos los test el programa no inicia, para no tener que jugar cada vez que queremos testear
if not "pytest" in sys.modules:
    inicioPrograma()

