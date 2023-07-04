"""
El impuesto a cancelar por persona se rige de acuerdo al ingreso anual. Para ingresos menores iguales
a 3000bs es de 100bs, para ingresos superiores a 3000bs pero inferior a 10000bs es de 400bs y para ingresos
superiores a 10000 deberá cancelar en impuesto 650bs.
Importante, si la persona tiene 3 o más hijos bajo su responsabilidad recibirá un descuento del 27% del monto
a cancelar.

Desarrolle un programa en Python que permita  determinar el impuesto a cancelar por persona de acuerdo
a la cantidad de ingreso anual y la cantidad de hijos bajo su responsabilidad.
"""

seguir = "s"

while seguir == "s":

    ingreso_anual_str = input("Coloque su ingreso anual: ")
    ingreso_anual = int(ingreso_anual_str)

    cantidad_hijos = int(input("Coloque la cantidad de hijos bajo su responsabilidad: "))

    impuesto = 0
    descuento = 0

    if ingreso_anual <= 3000:
        impuesto = 100
    elif ingreso_anual > 3000 and ingreso_anual <= 10000:
        impuesto = 400
    else:
        impuesto = 650

    if cantidad_hijos >= 3:
        descuento = (27 / 100) * impuesto

    impuesto_total_a_cancelar = impuesto - descuento
    
    print(f"Impuesto: {impuesto} bs")
    print(f"Descuentoe: {descuento} bs")
    print(f"Monto total de impuesto a cancelar es de: {impuesto_total_a_cancelar} bs")
    print("____________")

    seguir = input("'s' para seguir en el programa: ")
    