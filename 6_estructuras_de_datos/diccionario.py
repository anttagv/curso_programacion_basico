# Diccionario

diccionario = {"nombre":"Antonio","apellido":"Torres","edad":28}

diccionario['anho_nacimiento'] = 1995                   # Asignación de una nueva clave vlalor

nombre = diccionario['nombre']                          # Obtenemos el valor asociado a la clave suministrada

del diccionario["edad"]                                 # Eliminar un clave:valor de de acuerdo a la clave
                                                        # suministrada

lista_claves = list(diccionario)                        # Obtenemos la lista de las claves

esta_clave_en_diccionario = "nombre" in diccionario     # Determinamos si una clave está en el diccionario


diccionario_dos = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

diccionario_tres = dict(sape=4139, guido=4127, jack=4098)