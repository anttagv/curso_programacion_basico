

def formato_dato_persona(id: int, nombre: str, apellido: str, edad: str, /) -> dict:
    return {"id": id, "nombre": nombre, "apellido": apellido, "edad": edad}

def formato_dato_persona_archivo(datos: dict) -> str:
    id = datos["id"]
    nombre = datos["nombre"]
    apellido = datos["apellido"]
    edad = datos["edad"]
    return f"{id}|{nombre}|{apellido}|{edad}"

def formato_archivo_a_dato_persona(dato_archivo: str) -> dict:
    lista_datos = dato_archivo.split("|")

    id = int(lista_datos[0])
    nombre = lista_datos[1]
    apellido = lista_datos[2]
    edad = int(lista_datos[3])

    dato_persona = formato_dato_persona(id, nombre, apellido, edad)
    
    return dato_persona

def formato_mostrar_datos_por_consola(datos: dict) -> str:
    id = str(datos["id"])
    nombre = datos["nombre"]
    apellido = datos["apellido"]
    edad = str(datos["edad"])

    linea_consola = f"{id:4} {nombre:10} {apellido:10} {edad:5}"

    return linea_consola