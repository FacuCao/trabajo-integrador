"""class cuenta:
  def __init__(self,titular,cantidad):
		self.titular = titular
		self.__cantidad = cantidad
                
  def imprimir(self):
        print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)  

cuenta(self,)  """        

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    def mostrar(self):
        return "Cuenta\n" + "Titular: " + self.titular + " - Cantidad: " + str(self.cantidad)
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
    
    def retirar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad

titular = str(input("ingrese nombre del titular: "))
ingresar = int(input("cantidad ingresada: "))
retirar = int(input("que cantidad desea retirar?: "))


c1 = Cuenta("",10000)
print(c1.mostrar())
c1.ingresar()
print(c1.mostrar())
c1.retirar()
print(c1.mostrar())
c1.ingresar()
print(c1.mostrar())
c1.retirar()
print(c1.mostrar())            
