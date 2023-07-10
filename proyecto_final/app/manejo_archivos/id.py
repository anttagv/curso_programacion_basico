import os
import json

ruta = os.path.join("app/archivos/id.txt")

def leer_id() -> int:
    with open(ruta,"r",encoding="utf-8") as archivo:
        try:
            id = json.load(archivo)
            return id
        except:
            return 0

def generar_id() -> int:
    id = leer_id()
    id = id + 1
    with open(ruta, "w", encoding='utf-8') as archivo:
        json.dump(id,archivo)
    return id
