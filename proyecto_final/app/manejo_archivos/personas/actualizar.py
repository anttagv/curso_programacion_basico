import os
from app.manejo_archivos.personas.leer import leer
from app.formatos.formato_persona import formato_dato_persona_archivo

ruta = os.path.join("app/archivos/personas.txt")

def actualizar(datos: dict):

    personas = leer()

    for persona in personas.copy():
        if persona["id"] == datos["id"]:
            persona["nombre"] = datos["nombre"]
            persona["apellido"] = datos["apellido"]
            persona["edad"] = datos["edad"]
            break

    personas_str = ''
    for persona in personas:
        linea = formato_dato_persona_archivo(persona)
        personas_str = f"{personas_str}{linea}\n"
    
    with open(ruta, "w", encoding='utf-8') as archivo:
        archivo.write(personas_str)