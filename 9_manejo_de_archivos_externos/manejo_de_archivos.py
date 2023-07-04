import os

path_id = os.path.join("manejo_de_archivos/id.txt")

def incrementar_id():
    with open(path_id,'r+',encoding='utf-8') as archivo:
        for linea in archivo:
            id = int(linea.split("-")[1])
        archivo.truncate(0)
        id +=1
    with open(path_id,'r+',encoding='utf-8') as archivo:
        archivo.write(f"id-{id}")
        
def leer_id() -> int:
    with open(path_id,'r+',encoding='utf-8') as archivo:
        for linea in archivo:
            id = int(linea.split("-")[1])
        return id
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def formato_linea(id: int, nombre: str, /) -> str:
    return f"{id}|{nombre}\n"

def formato_persona(linea:str, /) -> dict:
    elementos = linea.split("|")
    id = elementos[0]
    nombre = elementos[1][:-1]
    return {"id":int(id),"nombre":nombre}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

path = os.path.join("manejo_de_archivos/personas.txt")
def crear(nombre : str, / ):
    with open(path,'r+',encoding='utf-8') as archivo:
        print(archivo.read())
        return
        id = leer_id()
        incrementar_id()
        archivo.write(formato_linea(id,nombre))
        

def leer() -> list:
    personas = []
    with open(path,'r+',encoding='utf-8') as archivo:
        for linea in archivo:
            personas.append(formato_persona(linea))
    return personas

def eliminar(id:int, /):
    with open(path,'r+',encoding='utf-8') as archivo:
        lineas = list(archivo)
        archivo.truncate(0)
    
    for linea in lineas.copy():
        if str(id) == linea.split("|")[0]:
            try:
                lineas.remove(linea)
            except:
                print("error en elmiminar")
            break

    with open(path,'r+',encoding='utf-8') as archivo:
        archivo.writelines(lineas)
              
def test():
    crear("Antonio Torres")
    #crear("José Sarmiento")
    #crear("Teresita Sarmiento")
    #crear("Valeria Gonzalez")
    
with open("manejo_de_archivos/test.txt",'r+',encoding='utf-8') as archivo:
    print("es:")
#test()
#eliminar(23)
#personas = leer()
#for persona in personas:
#    print(persona)