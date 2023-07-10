from app.formatos.formato_persona import formato_dato_persona
from app.manejo_archivos.id import generar_id

def ingresa_dato(id = -1) -> dict:
    
    print("")

    mensaje = "A continución, Ingrese los datos de una persona:"
    if id != -1:
        mensaje = "A continución, Ingrese los datos que desea actualizar:"
    print(mensaje)

    if id == -1:
        id = generar_id()

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    print("")

    return formato_dato_persona(id, nombre, apellido, edad)


def ingresa_id() -> int:
    print("")
    id = int(input("Ingrese un id: "))
    return id