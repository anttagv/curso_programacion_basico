# Funciones

#def funt():
#    return
#print(type(funt()))

def suma(f : int ,g : int ,*jj,**fff) -> str:
    
    #print(type(jj))
    #print(type(fff))
    su = 0
    for j in jj:
        su += j
    
    for k,v in fff.items():
        su += v
    return f + g + su

lista = [2,4,2,3,3,2,1,2]
tupla = (2,4,2,3,3,2,1,2)

#print(suma(1,3,*lista,*tupla,**{"a":1,"b":4}))
print(suma(f = 1,g = 2))
print(suma.__annotations__)

