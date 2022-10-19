import os

class archivo:

    def cargarCaminos(self):
        if not os.path.isfile("misCaminos.txt"):
            return None
        file = open("misCaminos.txt","r+")
        texto = file.readlines()
        listaCaminos = texto
        file.close()
        return listaCaminos
    
    def quitarCaracter(self,lista,caracter):
        nlista = []
        for element in lista:
            cadena = element.replace(caracter,"")
            nlista.append(cadena)
        return nlista
