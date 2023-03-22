class cuenta:
  def __init__(self,titular,cantidad):
		self.titular = titular
		self.__cantidad = cantidad
                
  def imprimir(self):
        print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)  

cuenta(self,)            