class Nodo():
    def __init__(self,dato):
        self.__dato = dato
        self.__siguiente = None
    def getDato(self):
        return self.__dato
    def getSiguiente(self):
        return self.__siguiente
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

class Pila():
    def __init__(self,dim):
        self.__dimension = dim
        self.__tope = -1
        self.__cabeza = None
    def Insertar(self,elem):
        if not self.__tope == self.__dimension:
            nuevonodo = Nodo(elem)
            nuevonodo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevonodo
            self.__tope += 1
    def MostrarFactorial(self):
        sum = 1
        aux = self.__cabeza
        while aux != None:
            #print(aux.getDato())
            sum *= aux.getDato()
            aux = aux.getSiguiente()
        print(sum)

if __name__ == "__main__":
    UnaPila = Pila(10)
    numero = int(input("Ingrese un numero para dar su factorial: "))
    for i in range (1,numero+1):
        UnaPila.Insertar(i)
    UnaPila.MostrarFactorial()