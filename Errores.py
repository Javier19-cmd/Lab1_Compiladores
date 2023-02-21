# Clase para detectar errores.

def deteccion(regex):

    # Verificando que la expresión tenga paréntesis de apertura y cierre.
    if regex.count('(') != regex.count(')'):
        print("Error: La expresión regular no tiene paréntesis de cierre.")
        return False
    # Verificando que la expresión tenga letras.
    if not any(char.isalpha() for char in regex):
        print("Error: La expresión regular no tiene letras.")
        return False
    return True