# Control de flujo (condicional)
"""
print("Inicio del programa")

estado = "s"

while estado == "s":
    
    edad_str = input("Ingrese la su edad: ")
    edad = int(edad_str)

    if edad < 12:
        print("Es un niño")
    elif edad <= 20:
        print("Es un joven")
    elif edad < 60:
        print("Es un adulto")
    else:
        print("Adulto mayor")

    estado = input("Si desea seguir en el código, ingrese la letra s: ")

print("Fin del programa")
"""

contador = 0

print("Inicio del programa")

while contador <= 10:

    contador += 1
    #contador = contador + 1
    print(f"El contador va por: {contador}")

print("Fin del programa")