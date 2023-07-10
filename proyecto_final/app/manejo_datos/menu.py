from app.manejo_datos.manejo_datos import ingresa_dato, ingresa_id
from app.manejo_archivos.personas.crear import crear
from app.manejo_archivos.personas.leer import leer
from app.manejo_archivos.personas.actualizar import actualizar
from app.manejo_archivos.personas.eliminar import eliminar
from app.formatos.formato_persona import formato_mostrar_datos_por_consola

def menu():
    
    #while True:
        print("")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("")
        print("Presione:")
        print("- 1 para crear")
        print("- 2 para leer")
        print("- 3 para actualizar")
        print("- 4 para eliminar")
        print("")

        opcion = -1
        try:
            opcion = int(input("Ingrese la opción: "))
            print("")
        except:
            pass

        if opcion == 1:
            datos_persona = ingresa_dato()
            crear(datos_persona)
            print("Persona agregada exitosamente!")

        elif opcion == 2:
            personas = leer()
            print("{0:4} {1:10} {2:10} {3:5}".format("Id", "Nombre", "Apellido" , "Edad"))
            for persona in personas:
                print(formato_mostrar_datos_por_consola(persona))
        
        elif opcion == 3:
            id_actualizar = ingresa_id()
            datos_persona_actualizar = ingresa_dato(id_actualizar)
            actualizar(datos_persona_actualizar)
            print("Datos actualizados exitosamente!")
        
        elif opcion == 4:
            id_eliminar = ingresa_id()
            eliminar(id_eliminar)
            print("Datos eliminados exitosamente!")
        
        else:
            print("Opción no encontrada")

        print("")
        print("------------------------------")
