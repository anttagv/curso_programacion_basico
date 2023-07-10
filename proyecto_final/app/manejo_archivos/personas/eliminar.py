import os
from app.manejo_archivos.personas.leer import leer
from app.formatos.formato_persona import formato_dato_persona_archivo

ruta = os.path.join("app/archivos/personas.txt")

def eliminar(id: int, /):
    
    personas = leer()

    for persona in personas.copy():
        if id  == persona["id"]:
            personas.remove(persona)
            break

    personas_str = ''
    for persona in personas:
        linea = formato_dato_persona_archivo(persona)
        personas_str = f"{personas_str}{linea}\n"
    
    with open(ruta, "w", encoding='utf-8') as archivo:
        archivo.write(personas_str)