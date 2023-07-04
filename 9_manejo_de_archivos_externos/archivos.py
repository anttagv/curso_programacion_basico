import os

ruta = os.path.join("archivo.txt")

#archivo = open(ruta, "r", encoding="utf-8")
#archivo.close()

with open(ruta, "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    linea = archivo.readline()
    todo = archivo.read()
    todo_10 = archivo.read(10)
    for linea in archivo:
        print(linea,end='')

with open(ruta, "w", encoding="utf-8") as archivo:
    agregar = input("Agregue una informacion: ")
    archivo.write(agregar)

with open(ruta, "a", encoding="utf-8") as archivo:
    agregar = input("Agregue una informacion: ")
    archivo.write(f"{agregar}\n")

