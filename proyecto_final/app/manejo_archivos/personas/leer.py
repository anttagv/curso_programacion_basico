import os
from app.formatos.formato_persona import formato_archivo_a_dato_persona

ruta =  os.path.join("proyecto_final/app/archivos/personas.txt")

def leer() -> list:
    personas = []

    with open(ruta,"r",encoding="utf-8") as archivo:
        for persona in archivo:
            personas.append(formato_archivo_a_dato_persona(persona))
    
    return personas