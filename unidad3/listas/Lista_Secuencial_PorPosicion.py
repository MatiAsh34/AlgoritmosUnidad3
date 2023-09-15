import numpy as np
class Lista_Secuencial():
    def __init__(self,dimension):
        self.__primero=999
        self.__ultimo=0
        self.__cant=0
        self.__dimension=dimension
        self.__lista=np.empty(self.__dimension,dtype=object)
        

    def cereo(self):
        self.__lista.fill(None)
    
    def vacia(self):
        return self.__cant == 0
        
    def llena(self):
        return self.__cant == self.__dimension
        
    def insertar(self,elem,posicion):
        p = posicion - 1
        if self.llena():
            print("esta llena")
        else:
            
            if p <= self.__dimension:
                if self.__ultimo <= p:
                    self.__ultimo = p
                    
                if self.__primero >= p:
                    self.__primero = p
                    
                if self.__lista[p] != None:
                    for i in range(self.__ultimo,p-1,-1):
                        self.__lista[i+1]=self.__lista[i]
                    self.__ultimo += 1
                        
            self.__lista[p]=elem
            self.__cant += 1
            
    def suprimir(self,posicion):
        p = posicion - 1
        if self.vacia():
            print("esta vacia")
        else:
            if self.__lista[p] != None:
                    for i in range(p,self.__ultimo,+1):
                        self.__lista[i]=self.__lista[i+1]
                    self.__lista[self.__ultimo] = None
                    self.__ultimo -= 1
                    self.__cant -= 1
                    
    def recuperar(self,posicion):
        p = posicion - 1
        i = 0
        if self.vacia():
            print("esta vacia")
        else:
            if p < self.__cant:
                while i != p:
                    i += 1
                return self.__lista[i]
            else:
                print("posicion fuera de rango!")
            
    def buscar(self,elem):
        i = 0
        if self.vacia():
            print("esta vacia")
        else:
            while i < self.__cant and elem != self.__lista[i]:
                i += 1
                print("i: ",i)
            if i == self.__cant:
                print("No se encontró el elemento!")
            else:
                print("El elemento esta en la posicion: ",i+1)
                    
                        
    def recorrer(self):
        print("primero",self.__primero)
        for i in range(self.__primero,self.__cant):
            print(self.__lista[i])
                    
if __name__ == '__main__':
    lista = Lista_Secuencial(6)
    lista.cereo()
    lista.insertar(3,3)
    lista.insertar(1,1)
    lista.insertar(2,2)
    lista.insertar(4,4)
    lista.insertar(77,4)
    lista.insertar(50,2)
    lista.recorrer()
    
    
    