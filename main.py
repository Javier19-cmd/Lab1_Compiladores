from reg import evaluar
from Thompson import thompson, graficar, grafo
from Errores import *

inp = input("Ingrese la expresion regular: ")

regex = evaluar(inp)

verificacion = deteccion(regex)

if verificacion == True:
    print("La expresion regular es correcta.")
    print("La expresion regular es: ", regex)
    automata, lista, diccionario = thompson(regex)
    graficar(automata, lista, diccionario)
    #grafo(automata, lista, diccionario)

else:
    print("La expresion regular es incorrecta.")