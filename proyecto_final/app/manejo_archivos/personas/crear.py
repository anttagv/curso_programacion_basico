import os
from app.formatos.formato_persona import formato_dato_persona_archivo

ruta = os.path.join("proyecto_final/app/archivos/personas.txt")

def crear(datos: dict):
    with open(ruta,"a",encoding="utf-8") as archivo:
        datos_persona_archivo = formato_dato_persona_archivo(datos)
        archivo.write(f"{datos_persona_archivo}\n")