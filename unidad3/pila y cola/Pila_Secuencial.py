import numpy as np

class pila:
    def __init__(self,dimension):
        self.__dimension = dimension
        self.__tope = -1
        self.__arreglo = np.empty(dimension, dtype=int)
        
    def vacia(self):
        return self.__tope == -1
    
    def insertar(self, x):
        if self.__tope < self.__dimension-1:
            self.__tope+=1
            self.__arreglo[self.__tope]=x
        
    def suprimir(self):
        if self.vacia():
            print("Pila vacia")
        else:
            self.__arreglo=np.delete(self.__arreglo,-1)
            self.__tope -= 1
        
    def mostrar(self):
        if self.vacia():
            print("Pila vacia")
        else:
            for i in range(self.__tope,-1,-1):
                print(self.__arreglo[i],end=' -> ')
                
if __name__ == '__main__':
    unapila = pila(5)
    unapila.insertar(1)
    unapila.insertar(2)
    unapila.insertar(3)
    unapila.insertar(4)
    unapila.insertar(5)
    unapila.mostrar()
    print("\n")
    unapila.suprimir()
    unapila.mostrar()
