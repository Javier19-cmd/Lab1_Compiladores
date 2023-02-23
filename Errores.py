import re

# Clase para detectar errores.

def deteccion(regex):

    # Verificando que la expresión tenga paréntesis de apertura y cierre.
    if regex.count('(') != regex.count(')'):
        print("Error: La expresión regular no tiene paréntesis de cierre.")
        return False
    
    # Verificando que la expresión tenga letras o números.
    coin = re.match(r"[a-zA-Z0-9]+", regex)

    if not coin:
        print("Error")
        #print("Error: La expresión regular no puede tener números y letras.")
        return False


    # Verificando que la expresión no tenga un * o un + al inicio.
    coincidencia = re.match(r"^(?![*+]).*", regex)

    if not coincidencia:
        print("Error: La expresión regular no puede empezar con un * o un +.")
        return False
    
    # Verificando que la expresión no tenga un * o un + al final.
    return True