# Sentencia match. version 10 o superiores

status = 404

"""
match status:
    case 400:
        return "Bad request"
    case 404:
        return "Not found"
    case 418:
        return "I'm a teapot"
    case _:
        return "Something's wrong with the internet"
"""