import random
import math

#Tomas Pitinari
#COSAS A SABER:
#-La verificacion de que no se generen palabras iguales solo se hace al ingresar caracteres random en el tablero, por lo tanto
#si se ingresan dos palabras, "LLAMA" y "LLAMARADA", "LLAMA" puede llegar a aparecer 2 veces, una dentro de "LLAMARADA" y otra fuera.
#Como el enunciado no aclaraba del todo esas situaciones la forma de verificar esa condicion al ingresar las palabras dadas
#sin que aparezcan mas de una vez es agregar una condicion a ubicar_palabras, tal que al tomar una palabra random de posibilidades_palabras
#cuente cuantas veces aparece esa palabra en un tablero, generado por las posiciones_actuales y la posicion a verificar, y si la
#palabra aparece mas de una vez entonces se agrega a posiciones_probadas y se toma otra, de esta forma, el ejemplo de "LLAMA"
#y "LLAMARADA" con la misma direccion daria un tablero donde las mismas estarian superpuestas, y si tienen diferentes direcciones
#no se podrian ubicar las palabras de una forma valida
#
#-Un posible problema podria ser que las letras ingresadas en el tablero para rellenar son aleatorias y ubican letras al azar 
#hasta que un tablero es valido, hasta ahora en todos los casos que testee no encontre ningun fallo. Pero puede ser genere tableros
#continuamente sin solucion, pense una solucion que seria revisar para todas las posibles direcciones si esa letra forma una palabra
#y en caso de que se cumpla descartar la letra y probar otra, pero me parecio mas eficiente agregarlas aleatoriamente ya que
#imagine que son casos muy aislados.
#
#-Hice que el programa use mayusculas siempre por un tema de comodidad al leer, pero se puede cambiar a minusculas tranquilamente


#Se representan los datos como una lista de dos elementos, la dimension y una lista de listas que contiene las palabras con sus direcciones
#cargar_datos: Nada -> List
#Abre el archivo con los datos para el juego, primero toma la segunda linea donde se encuentra la dimension del tablero y luego toma de todas las lineas a partir de la 4ta de donde se
#consiguen las palabras y sus direcciones, finalmente devuelve todos los datos en una lista
def cargar_datos ():
	a = open("datos.txt","r")
	lineas = a.readlines()
	dimension = int(lineas[1])
	palabras = []
	for linea in lineas[3:]:
		palabras.append([linea[0:(len(linea)-3)],int(linea[len(linea)-2])])
	return [dimension,palabras]

#Se representan a las palabras como una lista de listas, tal que por cada elemento de la lista de listas es otra lista que contiene la palabra como un string y su direccion como un entero
#direcciones_moviento: List(List) -> Nada
#La funcion reemplaza el entero que representa la direccion por una tupla respectiva a cada numero que representa las unidades que se desplaza la palabra en (x,y)
def direcciones_movimiento (palabras):
	for palabra in palabras:
		if (palabra[1] == 0):
			palabra[1] = (1,0)
		elif (palabra[1] == 1):
			palabra[1] = (-1,0)
		elif (palabra[1] == 2):
			palabra[1] = (0,1)
		elif (palabra[1] == 3):
			palabra[1] = (0,-1)
		elif (palabra[1] == 4):
			palabra[1] = (1,1)
		elif (palabra[1] == 5):
			palabra[1] = (1,-1)

def test_direcciones_movimiento ():
	palabras = [["HOLA",4],["CHAU",0]]
	direcciones_movimiento(palabras)
	assert palabras == [["HOLA",(1,1)],["CHAU",(1,0)]]
	palabras = [["HOLA",1]]
	direcciones_movimiento(palabras)
	assert palabras == [["HOLA",(-1,0)]]

#Se representa la palabra como una lista de como una lista compuesta de un string y una tupla que determina su direccion
#largo_de_palabras: List(String,(Int,Int)) -> Int
#Toma una palabra en el formato dado y devuelve el largo de la misma, esta funcion esta declarada para poder ordenar con el metodo sort()
#entrada: ["HOLA",(1,1)] salida: 4
#entrada: ["SOL",(0,1)] salida: 3
def largo_de_palabras (palabra):	#esta funcion se define solo para poder usarla en el metodo sort de listas
	return len(palabra[0])

def test_largo_de_palabras ():
	assert largo_de_palabras(["HOLA",(1,1)]) == 4
	assert largo_de_palabras(["ANANA",(1,0)]) == 5
	assert not (largo_de_palabras(["MONTO",(0,1)]) == 4)

#Se representa la dimension como un numero entero y el tablero como una lista de lista de strings
#crear_tabla: Int -> List(List(String))
#La funcion va a tomar un valor entero positivo como parametro y va a devolver una lista de listas de largo nxn, inicializada con '-' en cada casilla
#entrada: 5 salida: [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
#entrada: 3 salida: [['-','-','-'],['-','-','-'],['-','-','-']]
def crear_tabla (dimension):
	tabla = []
	for x in range(0,dimension):
		tabla.append([])
		for y in range(0,dimension):
			tabla[x].append('-')
	return tabla

def test_crear_tabla ():
	assert crear_tabla(5) == [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
	assert crear_tabla(3) == [['-','-','-'],['-','-','-'],['-','-','-']]

#Se representara al lemario como un conjunto de Strings
#cargar_lemario: Nada -> set(String)
#La funcion va a leer todas las palabras de largo mayor a 1 (ya que sino serian solo letras) que se encuentre en el archivo lemario.txt y las va a agregar al conjunto
def cargar_lemario():
	lemario = set()
	a = open ("lemario.txt","r")
	for palabra_lemario in a.readlines():
		palabra_lemario = palabra_lemario.rstrip()
		if(len(palabra_lemario)>1):
			lemario.add(palabra_lemario.upper())
	return lemario

#Se representan las palabras como lista de listas que contienen los strings y su direccion, al lemario se los representa como un conjunto de Strings y la dimension como un Int
#validar_palabras_lemario: List(List((String,(Int,Int)))) -> set(String) -> Int -> Bool
#la funcion primero obtiene las palabras que estan en el lemario y no estan entre la lista de palabras, para que si se llega a reemplazar una palabra no pertenezca a la lista de palabras
#anteriores, luego revisa una a una si la palabra esta en el lemario y si tiene un largo adecuado, si la palabra cumple la condicion pasa a la siguiente palabra, si no lo cumple revisa si hay palabras disponibles en el lemario para reemplazar,
#si no hay mas palabras para reemplazar esta se eliminara de la lista de palabras, si hay palabras para reemplazar se va a elegir una palabra random del lemario y valido si puede entrar
#por su tamanio dentro del tablero, si no se cumple la validez sacara palabras random distintas hasta que una cumpla o hasta que no haya mas palabras por reemplazar y la palabra se eliminara,
#en caso que se cumpla se reemplazara la palabra, finalmente si luego de eliminar palabras no existen mas palabras la funcion retornara False como que no se puede jugar, caso contrario retornara True
#entrada: [["HOLA",(1,1)],["CHAU",(1,0)]] {"HOLA","CHAU","CASA","ANANA"} 4 salida: True
#entrada: [["HOLA",(1,1)],["CHAU",(1,0)]] {"CASA","ANANA"} 3 salida: False
def validar_palabras (palabras, lemario, dimension):
	palabras_set = set()
	for palabra in palabras:
		palabras_set.add(palabra[0])
	lemario_temp = list(lemario - palabras_set) #palabra con las que se puede reemplazar
	palabras_a_borrar = []
	for palabra in palabras:
		lemario_temp2 = lemario_temp
		if (((lemario & {palabra[0]}) == set()) or (len(palabra[0]) > dimension)): #revisa si la palabra no esta en el lemario o si no tiene un largo valido
			if(not lemario_temp == []):
				temp = random.choice(lemario_temp2) #si quedan palabras toma una aleatoria
				while (len(temp) > dimension):  
					lemario_temp2.remove(temp)  #si las palabras nuevas no tienen un largo valido sigue sacando
					if (lemario_temp2 == []):   #si ya no quedan palabras validas para reemplazar, la palabra se borra
						print(palabra[0] + " no se encuentra en el lemario, y no hay mas palabras en el lemario por cual reemplazar, por lo que la palabra se borrara y no habra reemplazo")
						palabras_a_borrar.append(palabra)
						break
					temp = random.choice(lemario_temp2)

				if (not lemario_temp2 == []):   #Si la palabra es valida se reemplaza y se saca de la lista del lemario para que no vuelva a tocar
					palabra[0]=temp
					lemario_temp.remove(temp)
			else:   #si directamente no hay palabras para reemplazar, se borrara la palabra
				print(palabra[0] + " no se encuentra en el lemario, y no hay mas palabras en el lemario, por lo que la palabra se borrara y no habra reemplazo")
				palabras_a_borrar.append(palabra)
	for palabra in palabras_a_borrar:
		palabras.remove(palabra)	#aca es donde se borran las palabras de antes

	if (palabras == []):	#si ya no hay palabras no se puede jugar
		return False
	return True

def test_validar_palabras():
	assert validar_palabras([["HOLA",(1,1)],["CHAU",(1,0)]],{"HOLA","CHAU","CASA","ANANA"},4)
	assert not validar_palabras([["HOLA",(1,1)],["CHAU",(1,0)]],{"CASA","ANANA"},3)

#Se representan las palabras como lista de listas que contienen los strings y su direccion, al lemario se los representa como un conjunto de Strings, la dimension como un Int y
#posiciones_actuales es una lista con n (siendo n la cantidad de palabras) elementos vacios
#ubicar_palabras: List(List(String,(Int,Int))) -> Int -> List((Int,Int)) -> Bool
#La funcion va a utilizar un indice para moverse entre las palabras y todas sus listas asociadas (posiciones_actuales, posibilidades_palabras, posiciones_probadas)
#ya que el orden de las palabras no va a cambiar dentro de las listas, por cada palabras va a calcular las posibilidades en donde se puede poner esa palabra en la grilla
#y se guardara en posibilidades_palabras, luego vemos si las posibilidades son nulas o si ya se cubrieron todas las posiciones posibles, si sigue habiendo posibilidades
#se tomara una posibilidad random se agregara a posiciones_probadas y posiciones_actuales y se pasara hacia la siguiente palabra repitiendo el procedimiento,
#por otro lado si se agotaron las posibilidades, se volvera a la palabra anterior para tomar otra posibilidad. Si el indice llega a -1 significa que no pudo
#ubicar las palabras de ninguna forma, por lo que devolvera False indicando que no se pudieron ubicar, por otro lado si el indice llega a ser igual a la cantidad
#de palabras, significa que ya pudo ubicar la palabras y que este es un tablero posible retornando True. Devolviendo un tablero dado por posiciones_actuales
#entrada: [["HOLA",(1,1)],["CHAU",(1,0)]] 5 [(),()] salida: True
#entrada: [["HOLA",(1,1)],["CHAU",(1,0)]] 4 [(),()] salida: False
def ubicar_palabras (palabras,dimension,posiciones_actuales):
	#Se inicializan variables
	ind = 0
	posibilidades_palabras = []
	for i in range(0,len(palabras)):
		posibilidades_palabras.append(set())
	posiciones_probadas = []
	for i in range(0,len(palabras)):
		posiciones_probadas.append(set())
	#Se comienza a ubicar
	while ind < len(palabras):
		if (ind < 0):   #Llega aqui si y solo si no hay forma de ubicar las palabras en el tablero
			return False
		calcular_posibilidades_palabra(palabras,dimension,posiciones_actuales,posibilidades_palabras,ind)   #se calculan las posibilidades de la palabra con indice ind
		if ((posibilidades_palabras[ind] - posiciones_probadas[ind]) == set()): #si todas las posibilidades ya se probaron se vuelve a la palabra anterior y se resetean las variables de esta palabra
			posiciones_probadas[ind] = set()
			posibilidades_palabras[ind] = set()
			ind -= 1
			continue
		x = random.sample(posibilidades_palabras[ind]-posiciones_probadas[ind],1)[0]	#Se toma aleatoriamente una posicion en el tablero
		posiciones_probadas[ind].add(x)
		posiciones_actuales[ind] = x	#se registra la ubicacion
		ind += 1	#y se pasa a la siguiente palabra
	return True

def test_ubicar_palabras ():
	assert ubicar_palabras([["HOLA",(1,1)],["CHAU",(1,0)]],5,[(),()])
	assert not ubicar_palabras([["HOLA",(1,1)],["CHAU",(1,0)]],4,[(),()])

#Se representan las palabras como lista de listas que contienen los strings y su direccion, al lemario se los representa como un conjunto de Strings, la dimension como un Int,
#posiciones_actuales es una lista con n (siendo n la cantidad de palabras) con una tupla de dos Int que representa la posicion en una grilla, las posibilidades_palabras es una 
#lista de conjuntos que contienen tuplas de posibles posiciones en la grilla y ult es un Int que indica cual es la palabra actual como un indice
#calcular_posibilidades_palabra: List(List(String,(Int,Int))) -> Int -> List((Int,Int)) -> List(set((Int,Int))) -> Int -> Nada
#la funcion primero revisa si previamente ya se calcularon posibilidades para no tenes que volver a pasar por todos los casos y ahorrar tiempo, luego inicializa dos Int en 0
#que van a ir sumando de manera que abarquen todos los pares ordenados de (AxA) para A = {0,1,2,...,n}, estos pares ordenados son indices de una grilla donde deberian estar las
#palabras. Por cada par de enteros primero revisa si entrarian en la grilla iniciando en esa posicion y luego revisa si en caso de cruzarse con otras palabras si es valida la posicion,
#si ambas condiciones son validas se agrega el par ordenado de enteros al conjunto de posibilidades
def calcular_posibilidades_palabra(palabras,dimension,posiciones_actuales,posibilidades_palabras,ult):
	if (posibilidades_palabras[ult] == set()):  #no se modifica en caso de que ya tenga cosas, como para ahorrar pasos
		x = 0
		y = 0
		while x < dimension:
			while y < dimension:
				#chequea si la palabra esta dentro del tablero
				if ( ((x+(palabras[ult][1][0] * (len(palabras[ult][0])-1))) >= 0) and ((x+(palabras[ult][1][0] * (len(palabras[ult][0])-1))) < dimension) and ((y+(palabras[ult][1][1] * (len(palabras[ult][0])-1))) >= 0) and ((y+(palabras[ult][1][1] * (len(palabras[ult][0])-1))) < dimension)):
					if ( no_interfieren_otras_palabras (palabras, posiciones_actuales, ult, x ,y) ):	#luego si no molesta al cruzarse con otra palabra, si es que lo hace
						posibilidades_palabras[ult].add((x,y))  #si cumple ambas condiciones se agrega la posicion
				y += 1
			x += 1
			y = 0

def test_calcular_posibilidades_palabra():
	posibilidades_palabras = []
	for i in range(0,2):
		posibilidades_palabras.append(set())
	calcular_posibilidades_palabra([["HOLA",(1,1)],["CHAU",(1,0)]],4,[(0,0),()],posibilidades_palabras,1)
	assert posibilidades_palabras[1] == set()
	calcular_posibilidades_palabra([["HOLA",(1,1)],["CHAU",(1,0)]],4,[(),()],posibilidades_palabras,0)
	assert posibilidades_palabras[0] == {(0,0)}
	calcular_posibilidades_palabra([["HOLA",(1,1)],["CHAU",(1,0)]],5,[(0,0),()],posibilidades_palabras,1)
	assert posibilidades_palabras[1] == {(1,0),(1,3),(0,4),(1,4)}

#Se representan las palabras como lista de listas que contienen los strings y su direccion, a las posiciones_actuales como una lista con n (siendo n la cantidad de palabras) con una 
#tupla de dos Int que representa la posicion en una grilla, a ult como un Int que es el indice de la palabra actual en la lista de palabras y a "x", "y" como dos enteros que representan
#los indices en la grilla donde se quiere ubicar la palabra actual
#no_interfieren_otras_palabras: List(List(String,(Int,Int))) -> List((Int,Int)) -> Int -> Int -> Int -> Bool
#La funcion va revisando palabra a palabra si se puede cruzar con la palabra actual, si una sola no se puede la funcion retorna False indicando que no se puede ingresar la palabra con esos
#indices, si llega hasta el final significa que no interfiere con ninguna palabra y devuelve True
#entrada: [["HOLA",(1,1)],["CHAU",(1,0)]] [(1,0),()] 1 0 0 salida: True
#entrada: [["HOLA",(1,1)],["CHAU",(1,0)]] [(0,0),()] 1 0 0 salida: False
def no_interfieren_otras_palabras (palabras, posiciones_actuales, ult, x, y):
	if (ult == 0):
		return True
	else:
		for i in range(0,ult):  #los indices indican a cada palabra
			if (not dos_palabras_pueden_cruzar(palabras, i, ult, posiciones_actuales, x, y)):   #revisa si dos palabras se pueden cruzar, si es que se cruzan
				return False
		return True

def test_no_interfieren_otras_palabras ():
	assert no_interfieren_otras_palabras([["HOLA",(1,1)],["CHAU",(1,0)]],[(),()],0,0,0)
	assert no_interfieren_otras_palabras([["HOLA",(1,1)],["CHAU",(1,0)]],[(1,0),()],1,0,0)
	assert not no_interfieren_otras_palabras([["HOLA",(1,1)],["CHAU",(1,0)]],[(0,0),()],1,0,0)
	assert no_interfieren_otras_palabras([["HOLA",(1,1)],["CHAU",(1,0)]],[(0,0),()],1,1,3)

#Se representan las palabras como lista de listas que contienen los strings y su direccion, i y ult se representan como Int, ambos indican los indices de las palabras para analizar si se pueden
#cruzar, posiciones_actuales como una lista con n (siendo n la cantidad de palabras) con una tupla de dos Int que representa la posicion en una grilla y finalmente "x" e "y" como Int que 
#representan la posicion a analizar de la palabra con indice ult
#dos_palabras_pueden_cruzar: List(List(String,(Int,Int))) -> Int -> Int -> List((Int,Int)) -> Int -> Int -> Bool
#Se crean dos diccionarios que como clave tienen la tupla con las coordenadas por donde pasa cada una de las palabras y como valor el respectivo caracter por el que pasa la palabra en esa coordenada.
#Luego se revisa por cada una de las claves de uno de los dos diccionarios si existe una clave igual en el otro diccionario, y si existe y los diccionarios en la misma clave no son iguales entonces 
#la funcion retorna False lo que quiere decir que esas dos palabras no se pueden cruzar, si pasa por todas las claves sin interferir, entonces retorna True, indicando que se pueden cruzar
#entrada:[["HOLA",(1,1)],["CHAU",(1,0)],["CASA",(1,0)]] 0 2 [(1,0),(1,1),()] 1 3 salida: True
#entrada:[["HOLA",(1,1)],["CHAU",(1,0)],["CASA",(1,0)]] 0 2 [(1,0),(1,1),()] 3 1 salida: True
#entrada:[["HOLA",(1,1)],["CHAU",(1,0)],["CASA",(1,0)]] 1 2 [(1,0),(1,1),()] 3 1 salida: False 
def dos_palabras_pueden_cruzar (palabras, i, ult, posiciones_actuales, x, y):
	xi = posiciones_actuales[i][0]
	yi = posiciones_actuales[i][1]
	coor_1 = {}
	coor_2 = {}
	for j in range(0,len(palabras[ult][0])):
		coor_1[(x,y)] = palabras[ult][0][j] #guarda en el diccionario con las letras que aparecen en cada posicion
		x += palabras[ult][1][0]
		y += palabras[ult][1][1]

	for j in range(0,len(palabras[i][0])):
		coor_2[(xi,yi)] = palabras[i][0][j] #guarda en el diccionario con las letras que aparecen en cada posicion
		xi += palabras[i][1][0]
		yi += palabras[i][1][1]

	for key_1 in coor_1.keys():
		if(key_1 in coor_2.keys()): #revisa si hay claves en comun
			if(not coor_1[key_1] == coor_2[key_1]): #si las hay y sus valores no son iguales entonces no se pueden cruzar
				return False
	return True

def test_dos_palabras_pueden_cruzar():
	assert dos_palabras_pueden_cruzar([["HOLA",(1,1)],["CHAU",(1,0)],["CASA",(1,0)]],0,2,[(1,0),(1,1),()],1,3)
	assert dos_palabras_pueden_cruzar([["HOLA",(1,1)],["CHAU",(1,0)],["CASA",(1,0)]],0,2,[(1,0),(1,1),()],3,1)
	assert not dos_palabras_pueden_cruzar([["HOLA",(1,1)],["CHAU",(1,0)],["CASA",(1,0)]],1,2,[(1,0),(1,1),()],3,1)

#Se representan las palabras como lista de listas que contienen los strings y su direccion, posiciones_actuales como una lista con n (siendo n la cantidad de palabras) con una tupla de dos Int que 
#representa la posicion en una grilla y tablero es una lista de listas de Strings donde se van a ubicar las palabras
#colocar_en_tablero: List(List(String,(Int,Int))) -> List((Int,Int)) -> List(List(String)) -> Nada
#La funcion pasa palabra por palabra tomando sus posiciones de posiciones_actuales e ingresa caracter a caracter en el tablero, moviendose con la tupla de enteros que indica la direccion de la palabra.
#Modificando el tablero sin retornar nada
def colocar_en_tablero(palabras,posiciones_actuales,tablero):
	for i in range(0,len(palabras)):
		(x,y) = posiciones_actuales[i]
		for j in range(0,len(palabras[i][0])):
			tablero[y][x]=palabras[i][0][j]
			x += palabras[i][1][0]
			y += palabras[i][1][1]

def test_colocar_en_tablero():
	tablero = crear_tabla(5)
	colocar_en_tablero([["HOLA",(1,1)],["CHAU",(1,0)]],[(1,0),(0,0)],tablero)
	assert tablero == [['C','H','A','U','-'],['-','-','O','-','-'],['-','-','-','L','-'],['-','-','-','-','A'],['-','-','-','-','-']]
	tablero = crear_tabla(5)
	colocar_en_tablero([["HOLA",(1,1)],["CHAU",(1,0)]],[(0,0),(1,3)],tablero)
	assert tablero == [['H','-','-','-','-'],['-','O','-','-','-'],['-','-','L','-','-'],['-','C','H','A','U'],['-','-','-','-','-']]

#Se representa la lista como una lista de strings
#lista_a_string: List(String) -> String
#La funcion toma string a string de la lista y los va concatenando en uno solo, finalmente retorna el unico string
#entrada: ["HOLA","CHAU"] salida: "HOLACHAU"
#entrada: ["HOLA","CHAU","CASA"] salida: "HOLACHAUCASA"
def lista_a_string (lista):
	string = ''
	for x in lista:
		string += x
	return string

def test_lista_a_string():
	assert lista_a_string(["HOLA","CHAU"]) == "HOLACHAU"
	assert lista_a_string(["HOLA","CHAU","CASA"]) == "HOLACHAUCASA"

#Se representan las palabras como lista de listas que contienen los strings y su direccion, apariciones_palabras es un diccionario que va a tener las veces que aparece una palabra en un tablero
# y la dimension es un Int
#contar_apariciones_palabras: List(List(String,(Int,Int))) -> {String:Int} -> List(List(String)) -> Int -> Nada
#La funcion crea una lista de strings de todas las posibles direcciones en las que pueden haber palabras en un tablero y despues cuenta la cantidad de veces que cada palabra se encuentra en el tablero
#y se guarda en el diccionario con clave la palabra, por ejemplo, la palabra "aca" aparece 2 en "acaca"
def contar_apariciones_palabras (palabras, apariciones_palabras, tablero, dimension):
	lista_strings = []
	lista_temp = []
	lista_temp2 = []	#variables que vamos a usar
	string_temp = ''

	for fila in tablero:
		string_temp = lista_a_string(fila)	#Strings horizontales
		lista_strings.append(string_temp)
		lista_strings.append(string_temp[::-1])
	for x in range(0,dimension):
		for y in range(0,dimension):
			lista_temp.append(tablero[y][x])
		string_temp = lista_a_string(lista_temp)	#strings verticales
		lista_strings.append(string_temp)
		lista_strings.append(string_temp[::-1])
		lista_temp = []
	for x in range(0,(dimension-1)):
		x1 = x
		y1 = 0
		y2 = (dimension - 1)
		while (x1 < dimension):
			lista_temp.append(tablero[y1][x1])
			lista_temp2.append(tablero[y2][x1])		#strings diagonales que inician desde los bordes de arriba y abajo
			x1 += 1
			y1 += 1
			y2 -= 1
		string_temp = lista_a_string(lista_temp)
		lista_strings.append(string_temp)
		string_temp = lista_a_string(lista_temp2)
		lista_strings.append(string_temp)
		lista_temp = []
		lista_temp2 = []
	for y in range(1,(dimension-1)):
		y1 = y
		x1 = 0
		while (y1 >= 0):
			lista_temp.append(tablero[y1][x1])	#strings diagonales que inician del borde de la izquierda
			x1 += 1
			y1 -= 1
		string_temp = lista_a_string(lista_temp)
		lista_strings.append(string_temp)
		lista_temp = []
		y1 = y
		x1 = 0
		while (y1 < dimension):
			lista_temp.append(tablero[y1][x1])
			x1 += 1
			y1 += 1
		string_temp = lista_a_string(lista_temp)
		lista_strings.append(string_temp)
		lista_temp = []
	for palabra in palabras:
		cant = 0
		for string in lista_strings:
			cant += contar_string(string,palabra[0])	#revisa cuantas veces aparece cada palabra
		apariciones_palabras[palabra[0]] = cant

def test_contar_apariciones_palabras ():
	tablero = crear_tabla(5)
	colocar_en_tablero([["HOLA",(1,1)],["CHAU",(1,0)],["ANANA",(1,0)]],[(0,0),(1,3),(0,4)],tablero)
	apariciones = {}
	contar_apariciones_palabras([["HOLA",(1,1)],["CHAU",(1,0)],["ANANA",(1,0)]],apariciones,tablero,len(tablero))
	assert apariciones == {"ANANA":2,"HOLA":1,"CHAU":1} #ANANA aparece 2 veces ya que es palindromo
	tablero = crear_tabla(5)
	colocar_en_tablero([["HOLA",(0,1)],["CHAU",(1,0)],["ANANA",(1,1)]],[(4,1),(0,2),(0,0)],tablero)
	contar_apariciones_palabras([["HOLA",(0,1)],["CHAU",(1,0)],["ANANA",(1,1)]],apariciones,tablero,len(tablero))
	assert apariciones == {"ANANA":1,"HOLA":1,"CHAU":1} #ahora ANANA, aunque sea palindromo aparece una vez, ya que es diagonal de izquierda
														#a derecha, de arriba a abajo, y no se puede ingresar una palabra diagonal de derecha a izquierda,
														#de abajo a arriba

#Se representa a combinacion como un string y a la palabra como un string
#contar_string: String -> String -> Int
#La funcion compara para todos los substrings del largo de la palabra si son iguales a la palabra, si lo son suma uno a la cantidad de veces y termina retornando esa cantidad. Si el
#string es mas largo que la combinacion no va a entrar al while y va a devolver 0
#entrada: "AHOLAM" "HOLA" salida: 1
#entrada: "AAA" "AA" salida: 2
#entrada: "HOLA" "MONTE" salida: 0
def contar_string (combinacion, palabra):
	i = 0
	j = len(palabra)
	cant = 0
	while (j <= len (combinacion)):
		if(palabra == combinacion[i:j]):
			cant += 1
		i+=1
		j+=1
	return cant

def test_contar_string ():
	assert contar_string("AHOLAM","HOLA") == 1
	assert contar_string("AAA","AA") == 2
	assert contar_string("HOLA","MONTE") == 0

#Se representa al tablero como una lista de listas de strings
#rellenar_con_letras: List(List(String)) -> Nada
#La funcion pasa casilla por casilla preguntando si no tiene ninguna letra ya ingresada, en caso de no tenerla se le ingresa una letra random entre "A" y "Z"
def rellenar_con_letras(tablero):
	for y in range(0,len(tablero)):
		for x in range(0,len(tablero[y])):
			if (tablero[y][x] == '-'):
				tablero[y][x] = chr(random.randint(ord('A'),ord('Z')))

def main():
	#Inicializamos los datos y algunas variables
	datos = cargar_datos()
	dimension = datos[0]
	palabras = datos[1]
	tablero = crear_tabla(dimension)
	lemario = cargar_lemario()

	#Corroboramos si las palabras son validas por el lemario y si entran en la grilla, si no entran se cambian, si todas las palabras del lemario no son validas no se puede jugar
	if (not validar_palabras(palabras,lemario,dimension)):		#las palabras no son validas si son mas largas que la dimension o si no estan en el lemario
		print("El lemario no tiene ninguna palabra valida para la grilla")
		return 0

	direcciones_movimiento(palabras) #Se cambia el formato de las direcciones para que sea mas comodo en las proximas funciones
	palabras.sort(reverse=True,key=largo_de_palabras)	#Se ordena de mayor a menor (largo) las palabras, ya que una palabra larga es mas dificil de ubicar que una corta
	
	posiciones_actuales = []	#Se inicializa la lista que va a tener las posiciones de las palabras en el tablero
	for i in range(0,len(palabras)):
		posiciones_actuales.append(())

	if (not ubicar_palabras(palabras,dimension,posiciones_actuales)):	#Ubicar palabras modifica posiciones_actuales y si no hay forma posible de ubicar las palabras devuelve False
		print("No se pudieron ubicar las palabras")		#Si devuelve False no se pueden ubicar las palabras en el tablero, por lo tanto no se puede jugar y termina el programa
		return 0
	else:	#Si se pudieron ubicar las palabras seguimos
		colocar_en_tablero(palabras,posiciones_actuales,tablero)	#colocamos en el tablero las palabras en posiciones_actuales
		
		apariciones_palabras = {}	#Como ya tenemos una distribucion de palabras validas en un tablero, contamos cuantas veces aparece cada palabra para despues comparar con la cantidad de veces
		contar_apariciones_palabras(palabras, apariciones_palabras, tablero, dimension)	#que aparece la palabra al ingresar caracteres aleatorios
		
		tablero_valido = []	#inicializamos tablero_valido como para tener una copia del tablero que sabemos que es valido antes de que se le ingresen caracteres aleatorios
		for x in range(0,dimension):
			tablero_valido.append([])
			for y in range(0,dimension):
				tablero_valido[x].append(tablero[y][x])
		
		apariciones_al_rellenar = {} #Se inicializa el diccionario que va a contar de cuantas formas se puede contar la palabra despues de ingresar caracteres aleatorios
		while (True):	#El programa va a generar tablero con letras aleatorias hasta que uno sea valido, se que es ineficiente, pero seria un caso muy raro que no funcione
			rellenar_con_letras(tablero)	#Se ingresan letras aleatorias en el tablero
			contar_apariciones_palabras(palabras, apariciones_al_rellenar, tablero, dimension)	#Una vez rellenado el tablero cuento las apariciones de las palabras
			if (apariciones_palabras == apariciones_al_rellenar):	#Si la cantidad es la misma muestro el tablero y termino el programa
				break
			
			tablero = []	#Esto solo pasaria en caso de que al ingresar las letras aleatorias la cantidad de formas en las que se pueden leer las palabras cambie, por lo tanto
			for x in range(0,dimension):	#el tablero vuelve a la version estable que se tiene guardada en tablero_valido
				tablero.append([])
				for y in range(0,dimension):
					tablero[x].append(tablero_valido[y][x])
		
		#presentacion de los datos
		for fila in tablero:	#muestra tablero
			print(fila)
		
		for i in range(0,len(palabras)):	#por cada palabra se va a buscar cual es su direccion y se mostrara un mensaje adecuado
			if (palabras[i][1] == (1,0)):			   #filas									   #columnas
				print(palabras[i][0] + " (" + str(posiciones_actuales[i][1]+1) + "," + str(posiciones_actuales[i][0]+1) + ") Horizontal de izquierda a derecha")
			elif (palabras[i][1] == (-1,0)):
				print(palabras[i][0] + " (" + str(posiciones_actuales[i][1]+1) + "," + str(posiciones_actuales[i][0]+1) + ") Horizontal de derecha a izquierda")
			elif (palabras[i][1] == (0,1)):
				print(palabras[i][0] + " (" + str(posiciones_actuales[i][1]+1) + "," + str(posiciones_actuales[i][0]+1) + ") Vertical de arriba a bajo")
			elif (palabras[i][1] == (0,-1)):
				print(palabras[i][0] + " (" + str(posiciones_actuales[i][1]+1) + "," + str(posiciones_actuales[i][0]+1) + ") Vertical de abajo a arriba")
			elif (palabras[i][1] == (1,1)):
				print(palabras[i][0] + " (" + str(posiciones_actuales[i][1]+1) + "," + str(posiciones_actuales[i][0]+1) + ") Diagonal de izquierda arriba a derecha abajo")
			elif (palabras[i][1] == (1,-1)):
				print(palabras[i][0] + " (" + str(posiciones_actuales[i][1]+1) + "," + str(posiciones_actuales[i][0]+1) + ") Diagonal de izquierda abajo a derecha arriba")


main()
