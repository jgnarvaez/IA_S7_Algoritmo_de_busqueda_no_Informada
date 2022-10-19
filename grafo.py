from operator import mod
from nodo import *

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
    
    def informacionMatriz(self, prmMatriz):
        for elemento in prmMatriz:
            for nodo in elemento:
                print((nodo.nombre) + ', ' + str((nodo.peso)))
            print()

    def splitCaminos(self,lista,caracter):
        caminos = []
        objNodo = nodo(self,self)
        for element in lista:
            recorrido = []
            cad = element.split(caracter)
            recorrido.append(cad)
            listaNodos = []
            for i in range(len(recorrido)):
                if i % 2 == 0:
                    n = recorrido[0]
                    objNodo.nombre = n
                else:
                    objNodo.peso = (int)(recorrido[i])
                listaNodos.append(objNodo)
            caminos.append(listaNodos)
        return caminos

def obtenerLista(miMatriz, miNodo):
    for elemento in miMatriz:
        varNodo = elemento[0]
        if varNodo.nombre == miNodo:
            miLista = elemento
            miLista.pop(0)
            return miLista