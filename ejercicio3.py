texto = str(input(""))

quitar = ",.:;!\"' "
for caracter in quitar:   
 texto = texto.replace(caracter, "")
texto = texto.lower()
palabras = texto.split()
diccionario_frecuencias = {}
for palabra in palabras :
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
    else:
        diccionario_frecuencias[palabra] = 1

for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    print (f"la palabra '{palabra} tiene una frecuencia de {frecuencia}")           