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
    
class cola_concadenada():
    def __init__(self):
        self.__cantidad = 0
        self.__primero = None
        self.__ultimo = None
        
    def vacia(self):
        return self.__cantidad == 0
    
    def insertar(self,num):
        nuevoNodo = Nodo(num)
        nuevoNodo.setSiguiente(None)
        if self.__ultimo == None:
            self.__primero = nuevoNodo
        else:
            self.__ultimo.setSiguiente(nuevoNodo)
        self.__ultimo = nuevoNodo
        self.__cantidad += 1

    def suprimir(self):
        if self.vacia():
            print("Cola vacia")
        else:
            aux = self.__primero
            self.__primero = self.__primero.getSiguiente()
            del aux
            self.__cantidad -= 1

    def recorrer(self):
        aux = self.__primero
        while aux != None:
            print(aux.getDato(),end=' -> ')
            aux = aux.getSiguiente()


if __name__ == '__main__':
    unapila=cola_concadenada()
    unapila.insertar(1)
    unapila.insertar(2)
    unapila.insertar(3)
    unapila.insertar(4)
    unapila.insertar(5)
    unapila.recorrer()
    print('\n')
    unapila.suprimir()
    unapila.recorrer()
