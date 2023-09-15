import numpy as np
class Nodo:
    def __init__(self):
        self.__dato = None
        self.__siguiente = -1
        
    def getDato(self):
        return self.__dato
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setDato(self,num):
        self.__dato=num
    
    def setSiguiente(self,sig):
        self.__siguiente=sig

class EspacioPila:
    def __init__(self,dim):
        self.__disponible=0
        self.__dimension=dim
        self.__nodos=np.empty(self.__dimension,dtype=Nodo)
        for i in range(self.__dimension):
            self.__nodos[i]=Nodo() 
            self.__nodos[i].setSiguiente(i+1)  

    def sigdisponible(self):
        i=0
        while i<self.__dimension and self.__nodos[i].getDato()!=None:
            i+=1
        if self.__nodos[i].getDato()!=None:
            self.__disponible=-1
        else:
            self.__disponible=i
    
    def insertarprimero(self,num):
        if self.__disponible!=-1:
            i=self.__disponible
            self.__nodos[i].setDato(num)
            self.__nodos[i].setSiguiente(-1)
            self.sigdisponible()
        return i
    
    def insertar(self,num,cab):
        if self.__disponible!=-1:
            self.__nodos[self.__disponible].setDato(num)
            i=cab
            ant=i
            while i!=-1 and num>self.__nodos[i].getDato():
                ant=i
                i=self.__nodos[i].getSiguiente()
            if i!=-1:
                if i==cab:
                    self.__nodos[self.__disponible].setSiguiente(i)
                    return self.__disponible
                else:
                    self.__nodos[ant].setSiguiente(self.__disponible)
                    self.__nodos[self.__disponible].setSiguiente(i)
            else:
                self.__nodos[ant].setSiguiente(self.__disponible)
                self.__nodos[self.__disponible].setSiguiente(i)
    
    def suprimir(self,n,cab):
        i=cab
        ant=i
        while i!=-1 and n!=self.__nodos[i].getDato():
            ant=i
            i=self.__nodos[i].getSiguiente()
        if i!=-1:
            if i==cab:
                j=self.__nodos[i].getSiguiente()
                self.__nodos[i].setSiguiente(self.__disponible)
                self.__nodos[i].setDato(None)
                return j
            else:
                self.__nodos[ant].setSiguiente(self.__nodos[i].getSiguiente())
                self.__nodos[i].setDato(None)
        else:
            print("No se ha encontrado el elemento")
        self.sigdisponible()
    
    def recorrer(self,cab):
        i=cab
        while i!=-1:
            print(self.__nodos[i].getDato(),end=' ')
            i=self.__nodos[i].getSiguiente()
        print("\n")
            
                        
    
class Cabeza:
    def __init__(self,pila):
        self.__cabeza=-1
        self.__cant=0
        self.__espacio=pila
    
    def insertar(self,num):
        if self.__cabeza==-1:
            self.__cabeza=self.__espacio.insertarprimero(num)
        else:
            cab=self.__espacio.insertar(num,self.__cabeza)
            if isinstance(cab,int):
                self.__cabeza=cab
            self.__espacio.sigdisponible()
        self.__cant+=1
    
    def suprimir(self,n):
        cab=self.__espacio.suprimir(n,self.__cabeza)
        self.__cant-=1
        if isinstance(cab,int):
                self.__cabeza=cab
            
    def recorrer(self):
        self.__espacio.recorrer(self.__cabeza)
        
    
if __name__ == "__main__":
    pila=EspacioPila(10)
    lista1=Cabeza(pila)
    lista1.insertar(10)
    lista1.insertar(12)
    lista1.insertar(13)
    lista1.insertar(9)
    lista1.insertar(4)
    lista1.insertar(2)
    lista1.insertar(6)
    lista1.insertar(3)
    lista1.insertar(11)
    lista1.suprimir(13)
    lista1.suprimir(4)
    lista1.recorrer()