import os
import json

ruta = os.path.join("archivo_json.txt")

def agregar():
    with open(ruta, "w", encoding="utf-8") as archivo:
        datos = {"nombre": "Juan", "edad": 20}
        #archivo.write(json.dumps(datos))
        json.dump(datos,archivo)

def leer():
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        print(type(datos["edad"]))

agregar()
leer()