# Técnicas de iteración

lista = [2,3,5,7,8,9,12,15,17]
tupla = (-2,2,"abc",4,7.4,"w3")
conjunto = set(("a","b","c","d"))
diccionario = {"nombre":"Antonio","apellido":"Torres","edad":28}


# items() -> obtenemos la clave y su respectivo valor.
# Aplicable: [ diccionarios ]
for clave,valor in diccionario.items():
    print(clave,valor)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# enumerate() -> Obtenemos el índice posición junto a su valor correspondiente
# Aplicable: [ lista , tupla , conjunto , diccionario ]
for indice , valor in enumerate(lista):
    print(f"indice: {indice} | Valor: {valor}")

for indice , valor in enumerate(tupla):
    print(f"indice: {indice} | Valor: {valor}")

for indice , valor in enumerate(conjunto):
    print(f"indice: {indice} | Valor: {valor}")

for indice , clave in enumerate(diccionario):           # Retorna la clave por cada ciclo
    print(f"indice: {indice} | clave: {clave}")


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# zip() -> iterar sobre dos o más secuencias al mismo tiempo.
# Aplicable: [ lista , tupla , conjunto , diccionario ]
preguntas = ['nombre', 'apellido', 'color favorito']
respuestas = ['Antonio', 'Torres', 'marrón']
for q, a in zip(preguntas, respuestas):
    print('Cual es tu {0}?  es {1}.'.format(q, a))

# reversed() -> iterar sobre una secuencia en orden inverso.
# Aplicable: [ lista , tupla , diccionario ]
for valor in reversed(lista):
    print(f"Valor: {valor}")

for valor in reversed(tupla):
    print(f"Valor: {valor}")

for clave in reversed(diccionario):           # Retorna la clave por cada ciclo
    print(f"clave: {clave}")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# sorted() -> itera sobre una secuencia ordenada. Deben ser los elementos del mismo tipo
# Aplicable: [ listas , tuplas , conjuntos , diccionarios ]
for valor in sorted(lista):
    print(f"Valor: {valor}")

#for valor in sorted(tupla):
#    print(f"Valor: {valor}")

for valor in sorted(conjunto):
    print(f"Valor: {valor}")

for clave in sorted(diccionario):           # Retorna la clave por cada ciclo
    print(f"clave: {clave}")