def unicos(lista : list) -> list:
    return list(set(lista))

print("modulo") #declaración


nombre = "Antonio"
_apellido = "Torres"

if __name__ == "__main__":
    import sys
    unicos(list(map(lambda x: int(x),tuple(sys.argv[1].split(",")))))