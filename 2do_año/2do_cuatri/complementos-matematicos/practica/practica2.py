#! /usr/bin/python

# 2da Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

# Un disjointSet lo representaremos como un diccionario. 
# Ejemplo: {'A':1, 'B':2, 'C':1} (Nodos A y C pertenecen al conjunto 
# identificado con 1, B al identificado on 2)

grafo_lista =  (['A','B','C','D','E','F','G'],[('A','B'),('B','C'),('A','B'),('C','D'),('E','F')])

def make_set(lista):
    '''
    Inicializa una lista de vértices de modo que cada uno de sus elementos pasen a ser conjuntos unitarios. 
    Retorna un disjointSet.
    '''
    pass


def find(elem, disjoint_set):
    '''
    Obtiene el identificador del conjunto de vértices al que pertenece el elemento.
    '''
    pass


def union(id_1, id_2, disjoint_set):
    '''
    Dado dos identificadores de conjuntos de vértices, une dichos conjuntos.
    Retorna la estructura actualizada
    '''
    pass


def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas a través de un
    disjointSet.
    Ejemplo:
        Entrada: [['a','b','c','d'], [('a', 'b')]]  
        Salida: {'a': 0, 'b': 0, 'c': 1, 'd': 2}
    '''
    pass

def componentes_conexas_lista(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas, representadas como
    una lista de vértices.
    Ejemplo:
        Entrada: [['a','b','c','d'], [('a', 'b')]]
        Salida: [['a, 'b'], ['c'], ['d']]
    '''
    pass



def main():
    pass

if __name__ == '__main__':
    main()
