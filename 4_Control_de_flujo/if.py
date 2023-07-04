# Sentencia if

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Número negativo')
elif x == 0:
    print('El número es 0')
elif x == 1:
    print('El número es 1')
else:
    print('Número positivo mayor a 1.')