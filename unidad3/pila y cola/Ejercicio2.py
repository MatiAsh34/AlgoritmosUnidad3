class nodo:
    def __init__(self,dato):
        self.__dato = dato
        self.__siguiente = None
    def getDato(self):
        return self.__dato
    def getSiguiente(self):
        return self.__siguiente
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

class Pila:
    def __init__(self,dim):
        self.__dimension = dim
        self.__tope = -1
        self.__cabeza = None

    def vacia(self):
        return self.__tope == -1

    def Insertar(self,elem):
        if not self.__tope == self.__dimension-1:
            nuevonodo = nodo(elem)
            nuevonodo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevonodo
            self.__tope += 1
        else:
            print("Pila llena")

    def MostrarBinario(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getDato(),end='')
            aux = aux.getSiguiente()

    

if __name__ == "__main__":
    UnaPila = Pila(10)
    numero = int(input("Ingrese numero para dar su conversion a binario: "))
    while numero >  0:
        resto = numero % 2
        UnaPila.Insertar(resto)
        numero = numero // 2
    UnaPila.MostrarBinario()