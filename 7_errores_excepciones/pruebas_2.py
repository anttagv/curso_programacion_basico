class NombreError(BaseException):
    pass

class Nombre2Error(NombreError):#Excetion
    pass

try:
    raise Nombre2Error("Algo esta mal 2")
except Nombre2Error:# as ne:
    print("NombreError")
    #print(ne.args)
    #print(ne.__str__())
except NombreError:# as ne:
    print("Nombre2Error")


"""
class NombrePropioError(Exception):
    pass
    #def __str__(self):
    #    return 'error nombre propio prueba'

try:
    raise NombrePropioError("wwwwwwww")
except NombrePropioError as npError:
    print(npError.__str__())
    #print(npError.args)
    print(type(npError.args))
"""
#raise ZeroDivisionError("ddd")
"""
try:
    int("")
except ValueError as excep:
    print(excep.args)
    print(excep.__str__())
"""
"""
try:
    raise ZeroDivisionError("ddd")
except ZeroDivisionError as ex:
    print(type(ex))
    print(ex)
    print(ex.args)
    print(ex.__str__())
"""