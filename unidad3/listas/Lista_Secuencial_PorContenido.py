import numpy as np

class Lista_Secuencial():   
    def __init__(self,dimension):
        self.__ultimo=0
        self.__dimension=dimension
        self.__lista=np.empty(self.__dimension,dtype=int)
    
    def vacia(self):
        return self.__ultimo == 0
        
    def llena(self):
        return self.__ultimo == self.__dimension
        
    def insertar(self,elem):
        if self.llena():
            print("esta llena")
        else:
            i = 0
            while i < self.__ultimo and elem > self.__lista[i]:
                i+=1
            for j in range(self.__ultimo,i-1,-1):
                self.__lista[j+1]=self.__lista[j]
            self.__lista[i]=elem
            self.__ultimo += 1
            
    def suprimir(self,elem):
        if self.vacia():
            print("esta vacia")
        else:
            i = 0
            while i < self.__ultimo and elem != self.__lista[i]:
                i += 1
            if i == self.__ultimo:
                print("el elemento no esta en la lista")
            else:
                for j in range(i,self.__ultimo-1):
                    self.__lista[j]=self.__lista[j+1]
                self.__ultimo -= 1

    def recorrer(self):
        for i in range(0,self.__ultimo):
           print(self.__lista[i],end=' -> ')
                    
if __name__ == '__main__':
    lista = Lista_Secuencial(9)
    lista.insertar(3)
    lista.insertar(2)
    lista.insertar(1)
    lista.insertar(5)
    lista.insertar(4)
    lista.recorrer()
    lista.suprimir(3) #suprime por numero
    print("\n")
    lista.recorrer()
    