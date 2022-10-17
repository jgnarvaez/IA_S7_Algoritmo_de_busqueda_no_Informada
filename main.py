from grafo import *

objGrafo = grafo()
objNodo1 = nodo('S',0)
objNodo2 = nodo('A',3)
objNodo3 = nodo('B',1)
objNodo4 = nodo('C',8)
recorridoS = [objNodo1,objNodo2,objNodo3,objNodo4]

objNodo5 = nodo('A',0)
objNodo6 = nodo('D',3)
objNodo7 = nodo('E',7)
objNodo8 = nodo('G',15)
recorridoA = [objNodo5,objNodo6,objNodo7,objNodo8]

objNodo9 = nodo('B',0)
objNodo10 = nodo('G',20)
recorridoB = [objNodo9,objNodo10]

objNodo11 = nodo('C',0)
objNodo12 = nodo('G',5)
recorridoC = [objNodo11,objNodo12]

objGrafo.varMatriz.append(recorridoS)
objGrafo.varMatriz.append(recorridoA)
objGrafo.varMatriz.append(recorridoB)
objGrafo.varMatriz.append(recorridoC)

objGrafo.informacionMatriz(objGrafo.varMatriz)

solucion = objGrafo.ucs(objGrafo.varMatriz,'S','G')
print('La solucion es',solucion)
print('cost of solution is', costeCamino(solucion)[0])