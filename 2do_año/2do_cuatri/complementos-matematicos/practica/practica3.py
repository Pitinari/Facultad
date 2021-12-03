#! /usr/bin/python
# -*- coding: utf-8 -*-

# 3ra Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

"""
Recordatorio: 
- Un camino/ciclo es Euleriano si contiene exactamente 1 vez
a cada arista del grafo
- Un camino/ciclo es Hamiltoniano si contiene exactamente 1 vez
a cada vértice del grafo
"""


def esCaminoEuleriano(grafo, camino):
    """Comprueba si una lista de aristas constituye un camino euleriano
    en un grafo.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

        path (lista de aristas): posible camino
                                 Ej: [('a', 'b'), ('b', 'c')]

    Returns:
        boolean: path es camino euleriano en graph

    Raises:
        TypeError: Cuando el tipo de un argumento es inválido
    """
    pass


def esCicloEuleriano(grafo, ciclo):
    """Comprueba si una lista de aristas constituye un ciclo euleriano
    en un grafo.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

        path (lista de aristas): posible ciclo
                                 Ej: [('a', 'b'), ('b', 'c')]

    Returns:
        boolean: path es ciclo euleriano en graph

    Raises:
        TypeError: Cuando el tipo de un argumento es inválido
    """
    pass


def esCaminoHamiltoniano(grafo, camino):
    """Comprueba si una lista de aristas constituye un camino hamiltoniano
    en un grafo.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

        path (lista de aristas): posible camino
                                 Ej: [('a', 'b'), ('b', 'c')]

    Returns:
        boolean: path es camino hamiltoniano en graph

    Raises:
        TypeError: Cuando el tipo de un argumento es inválido
    """
    pass


def esCicloHamiltoniano(grafo, ciclo):
    """Comprueba si una lista de aristas constituye un ciclo hamiltoniano
    en un grafo.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

        path (lista de aristas): posible ciclo
                                 Ej: [('a', 'b'), ('b', 'c')]

    Returns:
        boolean: path es ciclo hamiltoniano en graph

    Raises:
        TypeError: Cuando el tipo de un argumento es inválido
    """
    pass


def tieneCaminoEuleriano(grafo):
    """Comprueba si un grafo no dirigido tiene un camino euleriano.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

    Returns:
        boolean: graph tiene un camino euleriano

    Raises:
        TypeError: Cuando el tipo del argumento es inválido
    """
    pass


class Graph:
    """Definimos esta clase como ayuda a la implementación del algoritmo de Fleury
    """

    def __init__(self, grafo_lista):
        """Inicializamos el grafo a partir de un grafo en representación de lista
        """

        self.V = grafo_lista[0]
        self.graph = self.listaADiccionario(grafo_lista)

    def listaADiccionario(self, grafo_lista):
        """Toma un grafo no dirigido en representación de lista y retorna un diccionario, en donde las claves
        son vértices y los valores son listas de vértices, representando cada una de las aristas. Por ejemplo:
        {'a': ['b', 'e'],..} representa la existencia de las aristas ('a','b') y ('a','e')
        """
        graph = {v: [] for v in grafo_lista[0]}
        for (u, v) in grafo_lista[1]:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def removerArista(self, u, v):
        """Dados dos vértices (u y v), elimina la arista (u,v) (y también la arista (v,u) puesto que es un grafo
        no dirigido)
        """
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def agregarArista(self, u, v):
        """Dados dos vértices (u y v), agrega la arista (u,v) (y también la arista (v,u) puesto que es un grafo
        no dirigido)"""
        self.graph[u].append(v)
        self.graph[v].append(u)

    def cantidadVerticesAlcanzables(self, v, visitados):
        """Cuenta la cantidad de vértices alcanzables desde v, haciendo una búsqueda en profundidad.
        El argumento visited es un diccionario en donde las claves son los vértices, y los valores
        corresponden a un booleano indicando si el vértice fue visitado o no.
        La primera vez que se llama al método, ningún vértice debe haber sido visitado.
        """
        count = 1
        visitados[v] = True
        for i in self.graph[v]:
            if not visitados[i]:
                count = count + self.cantidadVerticesAlcanzables(i, visitados)
        return count

    def esSiguienteAristaValida(self, u, v):
        """Determina si la arista (u,v) es elegible como próxima arista a visitar."""
        pass

    def printEuler(self, u):
        """Imprime un camino o ciclo euleriano comenzando desde el vértice u.
        """
        pass


def caminoEuleriano(grafo_lista):
    """Obtiene un camino euleriano en un grafo no dirigido, si es posible

    Argumentos:
        grafo: Grafo en formato de listas. 
                Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

    Retorno:
        lista de aristas: ciclo euleriano, si existe
        None: si no existe un camino euleriano
    """
    # Determinar el vértice de inicio v
    # grafo = Graph(grafo_lista)
    # grafo.printEuler(v)
    pass


def main():
    pass


if __name__ == '__main__':
    main()
