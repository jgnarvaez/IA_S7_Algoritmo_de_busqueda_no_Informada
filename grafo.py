from nodo import *
from numpy import *

# función que permite encontrar el coste de camino respecto a los caminos ingresados en la cola de prioridad.
# En cada posición de la cola de prioridad hay un camino desde el vértice inicial al final
def costeCamino(camino):
        totalCoste = 0
        for (nodo, coste) in camino:
            totalCoste += coste
        return totalCoste, camino[-1][0]

class grafo:
    varMatriz = []

    def __init__(self):
        pass

    def ucs(self, grafo, incio, objetivo):
        visitados = []
        colaPrioridad = [[(incio, 0)]]
        while colaPrioridad:
            # ordenamos por el coste del camino
            colaPrioridad.sort(key=costeCamino)
            camino = colaPrioridad.pop(0)  # elegimos el camino de menor coste
            nodo = camino[-1][0]
            if nodo in visitados:
                continue
            visitados.append(nodo)
            if nodo == objetivo:
                return camino
            else:
                # sucesores del nodo seleccionado
                nodosAdyacentes = obtenerLista(grafo, nodo)

                for element in nodosAdyacentes:
                    nuevoCamino = camino.copy()
                    nuevoCamino.append((element.nombre, element.peso))
                    colaPrioridad.append(nuevoCamino)

                #for (nodoAdyacente, coste) in nodosAdyacentes:
                 #   nuevoCamino = camino.copy()
                  #  nuevoCamino.append((nodoAdyacente, coste))
                   # colaPrioridad.append(nuevoCamino)
    
    def informacionMatriz(self, prmMatriz):
        for elemento in prmMatriz:
            for nodo in elemento:
                print((nodo.nombre) + ', ' + str((nodo.peso)))
            print()

def obtenerLista(miMatriz, miNodo):
    for elemento in miMatriz:
        varNodo = elemento[0]
        if varNodo.nombre == miNodo:
            miLista = elemento
            miLista.pop(0)
            return miLista