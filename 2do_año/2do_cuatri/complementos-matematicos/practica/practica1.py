#! /usr/bin/python

# 1ra Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

import sys

def lee_grafo_stdin():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
    pass


def lee_grafo_archivo(file_path):
    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
    pass


def imprime_grafo_lista(grafo):
    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''
    pass


def lista_a_incidencia(grafo_lista):
    '''
    Transforma un grafo representado por listas a su representacion 
    en matriz de incidencia.
    '''
    pass


def incidencia_a_lista(grafo_incidencia):
    '''
    Transforma un grafo representado una matriz de incidencia a su 
    representacion por listas.
    '''
    pass


def imprime_grafo_incidencia(grafo_incidencia):
    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de incidencia.
    '''
    pass


def lista_a_adyacencia(grafo_lista):
    '''
    Transforma un grafo representado por listas a su representacion 
    en matriz de adyacencia.
    '''
    pass


def adyacencia_a_lista(grafo_adyacencia):
    '''
    Transforma un grafo representado una matriz de adyacencia a su 
    representacion por listas.
    '''
    pass


def imprime_grafo_adyacencia(grafo_adyacencia):
    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de adyacencia.
    '''
    pass


#################### FIN EJERCICIO PRACTICA ####################
grafo_adyacencia1 = (
    ['A', 'B', 'C', 'D'], 
    [[0, 1, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0],]
)

grafo_adyacencia2 = (
    ['A', 'B', 'C', 'D'], 
    [[0, 2, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0],]
)

# import sys
def lee_entrada_0():
	count = 0
	for line in sys.stdin:
		count = count + 1
		print ('Linea: [{0}]'.format(line.strip()))
	print ('leidas {0} lineas'.format(count))

	
def lee_entrada_1():
	count = 0
	try:
		while True:
			line = input().strip()
			count = count + 1
			print ('Linea: [{0}]'.format(line))
	except EOFError:
		pass
	
	print ('leidas {0} lineas'.format(count))
   

def lee_archivo(file_path):
	print ('leyendo archivo: {0}'.format(file_path))
	count = 0

	with open(file_path, 'r') as f:
		first_line = f.readline()
		print ('primer linea: [{}]'.format(first_line))
		for line in f:
			count = count + 1
			#print 'Linea: [{0}]'.format(line)	
	print ('leidas {0} lineas'.format(count))


def main():
	lee_entrada_1()

if __name__ == '__main__':
    main()
