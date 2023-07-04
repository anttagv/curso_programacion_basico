class NombreError(Exception):
    pass
try:
    raise NombreError("ssssss ssss ssss")
except:
    raise

"""
def dividir(numerador,denominador) -> float:
    return numerador/denominador

def calcular(num_1,num_2) -> float:
    return dividir(num_1,num_2)

def ingresa_numero(mensaje_al_usuario = "",/) -> float:
    while True:
        try:
            numero = float(input(mensaje_al_usuario))
        except ValueError:
            print("No fue un número lo que se ingreso. Intentelo nuevamente.")
        else:
            return numero
        
def procesar_calculo() -> float:
    numerador = ingresa_numero("Ingrese el número del numerador: ")
    denominador = ingresa_numero("Ingrese el número del denominador: ")
    division = calcular(numerador,denominador)
    return division

try:
    division = procesar_calculo()
    #raise RuntimeError("error inesperado")
    #1/0
    #int("a")
    
except ZeroDivisionError as e:
    print("Ocurrio un error en la división")
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
except:
    print("sssssssssssssssssssssssssssssss")
    pass
else:
    print("Todo bien, todo correcto")
    print(f"El resultado de la división es: {division:.2f}")
finally:
    print("proceso finalizado")

"""
"""
try:
    raise BaseException("error BaseException")
except BaseException as exc:
    print("error controlado")
    #raise #relanzar el error
    #raise RuntimeError("error RuntimeError") from exc #excepción es consecuencia directa de otra
    raise RuntimeError("error RuntimeError") from None #deshabilitar el encadenamiento automático de excepciones
"""