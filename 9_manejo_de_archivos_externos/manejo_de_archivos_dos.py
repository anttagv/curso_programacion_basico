import os

path = os.path.join("manejo_de_archivos/personas.txt")
with open(path,'rb+') as archivo:
    archivo.write(b'jjjj')
    #print(archivo.readlines())
    #print(type(archivo.readlines()))

with open(path,'rb+') as archivo:
    print(archivo.read())


"""
25|Antonio Torres
26|José Sarmiento
27|Teresita Sarmiento
28|Valeria Gonzalez
"""