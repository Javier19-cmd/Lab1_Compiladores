from reg import evaluar
from Thompson import thompson, graficar
from Errores import *

inp = input("Ingrese la expresion regular: ")

regex = evaluar(inp)

verificacion = deteccion(regex)

if verificacion == True:
    print("La expresion regular es correcta.")
    print("La expresion regular es: ", regex)
    diagrama = thompson(regex)
    print("Diagrama en el main: ", diagrama)

    graficar(diagrama)

else:
    print("La expresion regular es incorrecta.")