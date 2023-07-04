a = 22_444_222
b = 44_232_332
porc = a / b * 100
formateo = 'El valor de a es: {}\nEl valor de b es: {}.\nEl porcentaje es: {:.4f}'.format(a,b,porc)
#print(repr(formateo))
#print(formateo)

var_1 = 'hhhh'
var_2 = "asasas"
valor = f"valor: {var_1!r:10}."
valor_2 = f"valor: {var_2=}."
valor_3 = f"valor: {a:10}."
print(valor)
print(valor_2)
print(valor_3)

for x in range(1, 112):
    print('{0:3d} {1:5d} {2:7d}'.format(x, x*x, x*x*x))