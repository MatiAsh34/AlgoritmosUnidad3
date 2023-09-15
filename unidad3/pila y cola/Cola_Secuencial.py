import numpy as np

class cola_secuencial():
    
    def __init__(self,dimension):
        self.__primero = 0
        self.__ultimo = 0
        self.__cantidad = 0
        self.__maximo = dimension
        self.__arreglo = np.empty(dimension, dtype=int)
    
    def vacia(self):
        return self.__cantidad == 0 
    
    def insertar(self, x):
        if self.__cantidad < self.__maximo:
            self.__arreglo[self.__ultimo] = x
            self.__ultimo = (self.__ultimo+1) % self.__maximo
            self.__cantidad += 1
        else:
            print("Cola llena")
        
    def suprimir(self):
        if self.vacia():
            print("Cola vacia")
        else:
            self.__primero = (self.__primero+1) % self.__maximo
            self.__cantidad -= 1
            
    def recorrer(self):
        if not self.vacia():
            i = self.__primero
            j = 0
            while j < self.__cantidad:
                print(self.__arreglo[i],end=' -> ')
                i = (i + 1) % self.__maximo
                j += 1
                
                
if __name__ == '__main__':
    unapila=cola_secuencial(5)
    unapila.insertar(1)
    unapila.insertar(2)
    unapila.insertar(3)
    unapila.insertar(4)
    unapila.insertar(5)
    unapila.recorrer()
    print('\n')
    unapila.suprimir()
    unapila.recorrer()
