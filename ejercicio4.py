def creador_diccionario(cadena):
  lista_1= cadena.split()
  dicc_1={}
  for i in lista_1:
    if i in dicc_1:
      dicc_1[i] +=1
    else:
      dicc_1[i]= 1
  return dicc_1

def contador_diccionario(diccionario):
  palabra_frecuente= ''
  cantidad=0
  for letras,valor in diccionario.items():
    if valor > cantidad:
      cantidad= valor
      palabra_frecuente= letras
  return palabra_frecuente,cantidad
entrada=input('Ingrese su cadena de caracteres: ')
print(creador_diccionario(entrada))
print(contador_diccionario(creador_diccionario(entrada)))