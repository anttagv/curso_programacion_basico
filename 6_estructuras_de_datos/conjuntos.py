# Conjuntos


conjunto_vacio = set()
conjunto_vacio_dos = {}     # No es un conjunto, es una tupla

conjunto = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

conjunto_dos = set([1,2,6,2,4,6,21,2])      # Se compone por elementos no repetidos

conjunto_tres = set((1,2,6,2,4,6,21,2))     # Se compone por elementos no repetidos

print(type(conjunto_tres))

nombre = set("antonioj")
apellido = set("sarmiento")

union = nombre | apellido                   # Union
interseccion = nombre & apellido            # Interseccion
diferencia = apellido - nombre              # Diferencia
diferencia_simetrica = nombre ^ apellido    # Diferencia simetrica

#print(union)
#print(interseccion)
#print(diferencia)
#print(diferencia_simetrica)