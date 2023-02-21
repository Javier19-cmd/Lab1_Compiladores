# Clase para detectar errores.

def deteccion(regex):

    # Verificando que la expresión tenga paréntesis de apertura y cierre.
    if regex.count('(') != regex.count(')'):
        print("Error: La expresión regular no tiene paréntesis de cierre.")
        return False
    # Verificando que la expresión tenga letras o números.
    elif not any(char.isalpha() for char in regex):
        print("Error: La expresión regular no tiene letras.")
        return False

    # Verificando que en la expresión no existan cosas como ++a o +a.
    for i in range(len(regex)):
        if regex[i] == '+' or regex[i] == '*':
            if i == 0:
                print("Error: La expresión regular no tiene letras.")
                return False
            elif regex[i - 1] == '+' or regex[i - 1] == '*':
                print("Error: La expresión regular no tiene letras.")
                return False
        
        elif regex[i] == '.': # Verificando que en la expresión no existan cosas como ..a o .a.
            if i == 0:
                print("Error: La expresión regular no tiene letras.")
                return False
            elif regex[i - 1] == '.':
                print("Error: La expresión regular no tiene letras.")
                return False

    #Verificando que la expresión no tenga cosas como a|
    for i in range(len(regex)):
        if regex[i] == '|':
            # El i debe ser un número impar para que sea una expresión regular válida.
            if i % 2 == 0:
                print("Error: La expresión regular no tiene letras.")
                return False
            elif regex[i - 1] == '|':
                print("Error: La expresión regular no tiene letras.")
                return False
    return True