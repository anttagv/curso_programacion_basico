lista_id = [3,15,7,23,16,19,5,10]
lista_diccionario = [
    {"id":7,"nombre":"Juan","edad":15},
    {"id":3,"nombre":"Carlos","edad":12},
    {"id":15,"nombre":"Ana","edad":23},
    {"id":5,"nombre":"María","edad":15},
    {"id":19,"nombre":"Pedro","edad":27},
    {"id":23,"nombre":"Javier","edad":23},
    {"id":10,"nombre":"Gabriela","edad":28},
    {"id":16,"nombre":"Valeria","edad":21},
]


texto_buscar = "tor"
lista_str = ["antonio","jose","torres","sarmiento"]

lista_resultado = []

for i, elemento in enumerate(lista_str):
    if texto_buscar in elemento:
        lista_resultado.append(elemento)

print(lista_resultado)