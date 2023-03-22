"""divisor = 0
suma = 0


def maximo_comun_divisor(a,b):
    while (divisor == a % b):
       suma=suma+a+b
       print(divisor)
       

a = int(input("ingrese valor de a: "))
b = int(input("ingrese el valor de b: "))
resultado = maximo_comun_divisor(a,b)

print("el maximo comun divisor entre {} y {} es {}" .format(a,b,resultado))"""

def maximo_comun_divisor(a, b):
	divisor = 0
	while(b > 0):
		divisor = b
		b = a % b
		a = divisor
	return a
 
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
 
print("El máximo común divisor de ", num1," y ", num2," es ", maximo_comun_divisor(num1, num2))