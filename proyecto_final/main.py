"""
- Desarrolle un programa en Python que permita a un usuario ingresar por consola el 
nombre, apellido y edad de una persona. Estos datos deberán ser almacenados en un 
archivo de texto. El usuario también podrá leer, actualizar y eliminar información de este 
archivo
"""

from app.manejo_datos.menu import menu

if __name__ == "__main__":
    menu()