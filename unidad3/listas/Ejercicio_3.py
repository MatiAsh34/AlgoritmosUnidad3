import numpy as np
import csv

class Area_Forestal():
    def __init__(self,nombre,superficie):
        self.__nombre = nombre
        self.__superficie = superficie
    def getSuperficie(self):
        return self.__superficie
    def getNombre(self):
        return self.__nombre

class Lista_Secuencial():
    def __init__(self,dimension):
        self.__ultimo=0
        self.__dimension=dimension
        self.__lista=np.empty(self.__dimension,dtype=Area_Forestal)
        
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
                while i < self.__ultimo and elem.getSuperficie() < self.__lista[i].getSuperficie():
                    i+=1
                for j in range(self.__ultimo,i-1,-1):
                    self.__lista[j+1]=self.__lista[j]
                self.__lista[i]=elem
            self.__ultimo += 1
            
    def suprimir(self,nombre):
        if self.vacia():
                print("esta vacia")
        else:
            i = 0
            while (i < self.__ultimo) and (nombre != self.__lista[i].getNombre()):
                i+=1
            if i == self.__ultimo:
                print("no encontrado")
            else:
                for j in range(i,self.__ultimo-1):
                    self.__lista[j]=self.__lista[j+1]
                self.__ultimo -= 1
        
            
    def recorrer(self):
        for i in range(0,self.__ultimo):
           print("Provinvia: {}, Superficie Afectada: {}".format(self.__lista[i].getNombre(),self.__lista[i].getSuperficie()))
                    
if __name__ == '__main__':
    lista = Lista_Secuencial(9)
    archivo=open ("C:\\Users\\lisan\\OneDrive\\2° Año\\Estructura de datos y algoritmos\\Listas\\superficies.csv",encoding='utf8')
    reader=csv.reader(archivo,delimiter=';')
    for fila in reader:
        plantaaux=Area_Forestal(fila[3],int(fila[6]))
        lista.insertar(plantaaux)
    lista.recorrer()
    lista.suprimir("Suprimir")
    print("ayuda")
    lista.recorrer()