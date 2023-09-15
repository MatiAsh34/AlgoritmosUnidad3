class Nodo:
    def __init__(self,num):
        self.__numero = num
        self.__siguiente = None
        
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__numero
  
class pila():
    def __init__(self,dimension):
        self.__dimension = dimension
        self.__tope = -1
        self.__cabeza = None
        
    def vacia(self):
        return self.__tope == -1
    
    def insertar(self,x):
        if self.__tope == self.__dimension-1:
            print("llena")
        else:
            unNodo=Nodo(x)
            unNodo.setSiguiente(self.__cabeza)
            self.__cabeza=unNodo
            self.__tope += 1
        
    def suprimir(self):
        if self.vacia():
            print("Pila vacia")
        else:
            aux = self.__cabeza
            self.__cabeza = self.__cabeza.getSiguiente()
            self.__tope -= 1
            del aux
        
    def mostrar(self):
        if self.vacia():
            print("Pila vacia")
        else:
            aux = self.__cabeza
            while aux != None:
                print(aux.getDato(),end=' -> ')
                aux = aux.getSiguiente()
        
if __name__=="__main__":
    pila1=pila(5)
    pila1.insertar(1)
    pila1.insertar(2)
    pila1.insertar(3)
    pila1.insertar(4)
    pila1.mostrar()
    pila1.suprimir()
    print("\n")
    pila1.mostrar()
    print("\n")