import os
import json

ruta = os.path.join("manejo_de_archivos/data_json_dos.txt")

def crear():
    with open(ruta,"a",encoding="utf-8") as archivo:
        archivo.truncate(0)
        """
        json.dump([
            {"id":33,"nombre":"Elias"},
            {"id": 34, "nombre": "Ana"},
            {"id": 35, "nombre": "Caleb"},
            {"id": 36, "nombre": "Paula"}
            ],
            archivo)
        """
        x = json.dumps(1)#{"id": 37, "nombre": "Antonio"}
        archivo.write(x)
        #print("- ",type(x))

def leer():
    with open(ruta,"r+",encoding="utf-8") as archivo:
        #print(archivo.read())
        data = json.load(archivo)
        #print(type(data))
        print(data)
        #print(type(data[0]))
        #print(int(data[0]['id']))

crear()
leer()