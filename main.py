from grafo import *
from archivo import *

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

# objArchivo = archivo()
# caminos = objArchivo.cargarCaminos()
# caminos = objArchivo.quitarCaracter(caminos,'\n')
# caminos = objGrafo.splitCaminos(caminos,",")
objGrafo2 = grafo()

objCiudad1 = nodo('Bucaramanga',0)
objCiudad2 = nodo('Medellin',383)
objCiudad3 = nodo('Tunja',282)
Bucaramanga = [objCiudad1,objCiudad2,objCiudad3]

objCiudad4 = nodo('Medellin',0)
objCiudad5 = nodo('Bucaramanga',383)
objCiudad6 = nodo('Tunja',413)
objCiudad7 = nodo('Bogota',415)
objCiudad8 = nodo('Manizales',229)
Medellin = [objCiudad4,objCiudad5,objCiudad6,objCiudad7,objCiudad8]

objCiudad9 = nodo('Tunja',0)
objCiudad10 = nodo('Bucaramanga',282)
objCiudad11 = nodo('Medellin',413)
objcidudad12 = nodo('Bogota',139)
Tunja = [objCiudad9,objCiudad10,objCiudad11,objcidudad12]

objCiudad13 = nodo('Bogota',0)
objCiudad14 = nodo('Tunja',139)
objCiudad15 = nodo('Medellin',415)
objCiudad16 = nodo('Manizales',293)
objCiudad17 = nodo('Ibague',209)
objCiudad18 = nodo('Neiva',322)
Bogota = [objCiudad13,objCiudad14,objCiudad15,objCiudad16,objCiudad17,objCiudad18]

objCiudad19 = nodo('Manizales',0)
objCiudad20 = nodo('Medellin',229)
objCiudad21 = nodo('Bogota',293)
objCiudad22 = nodo('Pereira',53.3)
Manizales = [objCiudad19,objCiudad20,objCiudad21,objCiudad22]

objCiudad23 = nodo('Pereira',0)
objCiudad24 = nodo('Manizales',53.3)
objCiudad25 = nodo('Armenia',49.2)
Pereira = [objCiudad23,objCiudad24,objCiudad25]

objCiudad26 = nodo('Armenia',0)
objCiudad27 = nodo('Pereira',49.2)
objCiudad28 = nodo('Ibague',75.5)
objCiudad29 = nodo('Cali',179)
Armenia = [objCiudad26,objCiudad27,objCiudad28,objCiudad29]

objCiudad30 = nodo('Ibague',0)
objCiudad31 = nodo('Armenia',75.5)
objCiudad32 = nodo('Bogota',209)
objCiudad33 = nodo('Neiva',210)
Ibague = [objCiudad30, objCiudad31, objCiudad32, objCiudad33]

objCiudad34 = nodo('Cali',0)
objCiudad35 = nodo('Armenia',179)
objCiudad36 = nodo('Popayan',141)
Cali = [objCiudad34, objCiudad35, objCiudad36]

objCiudad37 = nodo('Neiva',0)
objCiudad38 = nodo('Ibague',210)
objCiudad39 = nodo('Bogota',322)
objCiudad40 = nodo('Popayan',273)
objCiudad41 = nodo('Pasto',467)
Neiva = [objCiudad37, objCiudad38, objCiudad39, objCiudad40, objCiudad41]

objCiudad41 = nodo('Popayan',0)
objCiudad42 = nodo('Neiva',273)
objCiudad43 = nodo('Cali',141)
objCiudad44 = nodo('Pasto',249)
Popayan = [objCiudad41, objCiudad42, objCiudad43, objCiudad44]

objCiudad45 = nodo('Pasto',0)
objCiudad46 = nodo('Popayan',249)
objCiudad47 = nodo('Neiva',467)
Pasto = [objCiudad45, objCiudad46, objCiudad47]

objGrafo2.varMatriz.append(Bucaramanga)
objGrafo2.varMatriz.append(Medellin)
objGrafo2.varMatriz.append(Tunja)
objGrafo2.varMatriz.append(Bogota)
objGrafo2.varMatriz.append(Manizales)
objGrafo2.varMatriz.append(Pereira)
objGrafo2.varMatriz.append(Armenia)
objGrafo2.varMatriz.append(Ibague)
objGrafo2.varMatriz.append(Cali)
objGrafo2.varMatriz.append(Neiva)
objGrafo2.varMatriz.append(Popayan)
objGrafo2.varMatriz.append(Pasto)

# objGrafo.informacionMatriz(objGrafo.varMatriz)

solucion = objGrafo2.ucs(objGrafo2.varMatriz,'Bucaramanga','Pasto')
print('La solucion es',solucion)
print('cost of solution is', costeCamino(solucion)[0])