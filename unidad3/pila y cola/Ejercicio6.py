import random

class Cliente:
	def __init__(self):
		self.__espera=0
		self.__sig=None

	def setSiguiente(self,sig):
		self.__sig=sig

	def setTiempo(self):
		self.__espera+=1

	def getSiguiente(self):
		return self.__sig

	def getDato(self):
		return self.__espera

class Cajero:
	def __init__(self):
		self.__ocupado=0
		self.__clientes=0

	def CajeroLibre(self):
		return self.__ocupado

	def SetCajero(self,valor):
		self.__ocupado = valor

	def SumarCliente(self):
		self.__clientes+=1

	def getClientes(self):
		return self.__clientes

class Cola:
	def __init__(self):
		self.__cant=0
		self.__pr=None
		self.__ul=None

	def vacia(self):
		return self.__cant==0

	def insertar(self):
		nuevocelda=Cliente()
		nuevocelda.setSiguiente(None)
		if self.__ul==None:
			self.__pr=nuevocelda
		else:
			self.__ul.setSiguiente(nuevocelda)
		self.__ul=nuevocelda
		self.__cant+=1

	def suprimir (self):
		if self.vacia():
			print ("Lista vacía")
		else:
			if self.__pr!= None:
				aux=self.__pr
				self.__pr=self.__pr.getSiguiente()
				del aux
			else:
				self.__ul = None
			self.__cant-=1
			print("Cliente eliminado")

	def sumarespera(self):
		if not self.vacia():
			aux=self.__pr
			while aux!=None:
				aux.setTiempo()
				aux=aux.getSiguiente()

	def recorrer(self):
		if not self.vacia():
			aux=self.__pr
			while aux!=None:
				print(aux.getDato(),end='')
				aux=aux.getSiguiente()
		else:
			print ("La lista está vacía")



if __name__=='__main__':
	i=0
	tiempocajero=int(input("Ingrese tiempo maximo de demora del cajero: "))
	tiempocliente=int(input("Ingrese tiempo de demora en llegar un cliente: "))
	cajero1=Cajero()
	cola1=Cola()
	while i!=60:
		num=random.randint(0,1)
		if num<1/tiempocliente:
			cola1.insertar()
			print("Llego cliente")
		if cajero1.CajeroLibre()==0:
			if not cola1.vacia():
				cola1.suprimir()
				cola1.sumarespera()
				cajero1.SumarCliente()
				cajero1.SetCajero(1)
		i += 1

		if cajero1.CajeroLibre()==1 and i%tiempocajero==0:
			cajero1.SetCajero(0)

	print("Tiempo total: ", i)
	print("Clientes: ", cajero1.getClientes())
	print("Tiempo de espera: ",i/cajero1.getClientes())