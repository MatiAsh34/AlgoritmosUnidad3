import numpy as np
import csv

class Designacion():
    def __init__(self,año,cargo,instancia_tipo,materia,varones,mujeres):
        self.__año = año
        self.__cargo = cargo
        self.__instancia_tipo = instancia_tipo
        self.__materia = materia
        self.__varones = varones
        self.__mujeres = mujeres
    def getAño(self):
        return self.__año

class Lista_Secuencial():
    def __init__(self,dimension):
        self.__ultimo=0
        self.__dimension=dimension
        self.__lista=np.empty(self.__dimension,dtype=Designacion)
        

    def cereo(self):
        self.__lista.fill(None)
    
    def vacia(self):
        return self.__ultimo == 0
        
    def llena(self):
        return self.__ultimo == self.__dimension
        
    def insertar(self,elem):
        if self.llena():
            print("esta llena")
        else:
            if self.vacia():
                self.__lista[0] = elem
            else:
                i = 0
                while i < self.__ultimo and elem.getAño() > self.__lista[i].getAño():
                    i+=1
                for j in range(self.__ultimo,i-1,-1):
                    self.__lista[j+1]=self.__lista[j]
                self.__lista[i]=elem
            self.__ultimo += 1
            
    def MostrarConCargo(self,cargo):
        i = 0 
        sum = 0
        while i < self.__ultimo:
            if cargo == self.__lista[i].getCargo():
                sum += self.__lista[i].getMujeres()
        print("Cantidad de mujeres de ese cargo: ",sum)

    def MostrarConMateriaCargoAño(self,materia,cargo,año):
        i = 0
        sum = 0
        while i < self.__ultimo:
            if materia == self.__lista[i].getMateria() and cargo == self.__lista[i].getCargo() and año ==self.__lista[i].getAño():
                sum += self.__lista[i].getHombre()
                sum += self.__lista[i].getMujeres()
        print("Cantidad de agentes de esa materia, cargo y año son: ",sum)

    def recorrer(self):
        for i in range(0,self.__ultimo):
           print(self.__lista[i].getAño())
                    
if __name__ == '__main__':
    lista = Lista_Secuencial(9)
    archivo=open ("C:\\Users\\lisan\\OneDrive\\2° Año\\Estructura de datos y algoritmos\\Listas\\designacion.csv",encoding='utf8')
    reader=csv.reader(archivo,delimiter=',')
    for fila in reader:
        plantaaux=Designacion(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]),int(fila[5]))
        lista.insertar(plantaaux)
    lista.recorrer()
    cargo = input("Ingrese cargo")
    lista.MostrarConCargo(cargo)
    print("ayuda")
    materia = input("Ingrese materia")
    cargo = input("Ingrese cargo")
    año = input("Ingrese año")
    lista.MostrarConMateriaCargoAño(materia,cargo,año)
    lista.recorrer()
    