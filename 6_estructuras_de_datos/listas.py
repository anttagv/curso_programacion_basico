# Listas

lista = [1,2,4,7,8,9,13]
lista_dos = [53,35,57,7,23,67]

lista.append(30)                    # return None | Agrega un ítem al final de la lista.
#print(lista)

lista.extend(lista_dos)             # return None | Extiende la lista agregándole todos los ítems del iterable.
#print(lista)

lista.insert(2,99)                  # return None | Inserta un ítem en una posición dada. El primer argumento
                                    #              es el índice del ítem delante del cual se insertará
#print(lista)

lista.remove(57)                    # return None | Elimina el primer ítem de la lista cuyo valor sea el ingresado.
del lista[0]                        # return None | Elimina el elemento al que corresponda el indice ingresa.
#lista.remove(98)                   # ValueError, Elemento 98 No encontrado

ultimo_item_delete = lista.pop()    # Quita el ítem en la posición dada de la lista y lo retorna. Si no se
item_delete = lista.pop(4)          # especifica un índice, a.pop() quita y retorna el último elemento de la lista
#print(ultimo_item_delete)
#print(item_delete)

index = lista.index(2)              # Retorna el índice basado en cero del primer elemento cuyo valor sea igual
#index_error = lista.index(98)      # a x. Lanza una excepción ValueError si no existe tal elemento.

count = lista.count(7)              # Retorna el número de veces que x aparece en la lista
#print(count)

#lista.sort() ????

lista.reverse()                     # return None | Invierte los elementos de la lista in situ.
#print(lista)

copy = lista.copy()                 #Retorna una copia superficial de la lista. Equivalente a a[:].
#print(copy)

lista.clear()                       # return None | Elimina todos los elementos de la lista. Equivalente a
#print(lista)                                       del a[:].
