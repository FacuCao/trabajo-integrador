num1 = int(input("ingrese el valor de a: "))
num2 = int(input("ingrese el valor de b: "))  


n=2

while True:
      if (n % num1 == 0) and (n % num2 == 0):
        mcm=n
        break
      n+=1  
          
print("El máximo común multiplo de ", num1," y ", num2," es ", .format(mcm(num1, num2)))