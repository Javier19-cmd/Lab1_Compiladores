from Estado import *
from Automata import *
from Transiciones import *
import matplotlib.pyplot as plt

def thompson(expresion_regular):
    """Convierte una expresión regular en un autómata utilizando el algoritmo de Thompson"""
    stack = []
    lista = []
    diccionario = {}
    estados = 0

    for caracter in expresion_regular:
        if caracter == '|':
            # Obtener los dos últimos automatas del stack
            b = stack.pop()
            a = stack.pop()


            # Crear nuevos estados inicial y final
            inicio = Estado(estados)
            estados += 1
            fin = Estado(estados)
            estados += 1

            # Crear transiciones epsilon desde los nuevos estados inicial y final a los automatas a y b.

            # Creando las transiciones epsilon desde el estado inicial al estado inicial de a y b.
            nuevo1 = Transiciones(inicio, 'ε', a.get_estado_inicial())
            nuevo2 = Transiciones(inicio, 'ε', b.get_estado_inicial())
            nuevo3 = Transiciones(a.get_estado_final(), 'ε', fin)
            nuevo4 = Transiciones(b.get_estado_final(), 'ε', fin)

            # Crear el nuevo autómata y apilarlo en el stack  
            nuevo_automata = Automata(inicio, fin)
            
            # Agregando los nuevos estados a la lista de estados.
            lista.append(nuevo1)
            lista.append(nuevo2)
            lista.append(nuevo3)
            lista.append(nuevo4)

            # Guardando el nuevo automata en el stack.
            stack.append(nuevo_automata)

        elif caracter == '*':
            # Obtener el último automata del stack
            a = stack.pop()

            # Crear nuevos estados inicial y final
            inicio = Estado(estados)
            estados += 1
            fin = Estado(estados)
            estados += 1

            # Crear transiciones epsilon desde los nuevos estados inicial y final a los estados inicial y final del automata a
            n1 = Transiciones(inicio, 'ε', a.get_estado_inicial())
            n2 = Transiciones(inicio, 'ε', fin)
            n3 = Transiciones(a.get_estado_final(), 'ε', a.get_estado_inicial())
            n4 = Transiciones(a.get_estado_final(), 'ε', fin)

            # Crear el nuevo autómata y apilarlo en el stack
            nuevo_automata = Automata(inicio, fin)
            stack.append(nuevo_automata)

            # Agregando los nuevos estados a la lista de estados.
            lista.append(n1)
            lista.append(n2)
            lista.append(n3)
            lista.append(n4)

        elif caracter == '+':
            # Obtener el último automata del stack
            a = stack.pop()

            # Crear nuevos estados inicial y final
            inicio = Estado(estados)
            estados += 1
            fin = Estado(estados)
            estados += 1

            # Crear transiciones epsilon desde los nuevos estados inicial y final a los estados inicial y final del automata a
            
            nu1 = Transiciones(inicio, 'ε', a.get_estado_inicial())
            nu2 = Transiciones(a.get_estado_final(), 'ε', a.get_estado_inicial())
            nu3 = Transiciones(a.get_estado_final(), 'ε', fin)

            # Crear el nuevo autómata y apilarlo en el stack
            nuevo_automata = Automata(inicio, fin)
            stack.append(nuevo_automata)
            
            # Agregando los nuevos estados a la lista de estados.
            lista.append(nu1)
            lista.append(nu2)
            lista.append(nu3)

        elif caracter == '.':
            # Obtener los dos últimos automatas del stack
            b = stack.pop()
            a = stack.pop()

            # Obteniendo el estado final del autómata b. (segundo autómata)
            print(b.get_estado_final())

            # Obteniendo el estado inicial del autómata a. (primer autómata)
            print(a.get_estado_inicial())

            # Buscando las transiciones del estado a.
            for i in lista:
                if i.getEstadoInicial() == b.get_estado_inicial():
                    # Creando una transición desde el estado inicial del autómata a al estado final del autómata b.
                    n = Transiciones(a.get_estado_final(), i.getSimbolo(), b.get_estado_final())
                    # Eliminando la transición del estado inicial del autómata b.
                    lista.remove(i)
                    # Agregando la nueva transición a la lista de transiciones.
                    lista.append(n)

            # Crear el nuevo autómata y apilarlo en el stack
            nuevo_automata = Automata(a.get_estado_inicial(), b.get_estado_final())
            stack.append(nuevo_automata)

            # # Crear el nuevo autómata y apilarlo en el stack
            # nuevo_automata = Automata(a.estado_inicial, b.estado_final)
            
            # stack.append(nuevo_automata)
            # lista.append(nuevo_automata)
        
        elif caracter == '?': # Operador de cero o una ocurrencia.
            # Obtener el último automata del stack
            a = stack.pop()

            # Crear nuevos estados inicial y final
            inicio = Estado(estados)
            estados += 1
            fin = Estado(estados)
            estados += 1

            # Crear transiciones epsilon desde los nuevos estados inicial y final a los estados inicial y final del automata a
            ne1 = Transiciones(inicio, 'ε', a.get_estado_inicial())
            ne2 = Transiciones(inicio, 'ε', fin)
            ne3 = Transiciones(a.get_estado_final(), 'ε', fin)

            # Crear el nuevo autómata y apilarlo en el stack
            nuevo_automata = Automata(inicio, fin)
            stack.append(nuevo_automata)
            
            # Guardando las transiciones de la forma (estado_inicial, caracter, estado_final) en un diccionario.
            lista.append(ne1)
            lista.append(ne2)
            lista.append(ne3)

        else:
            # Crear nuevos estados inicial y final para el autómata que representa el caracter actual.
            # Crear nuevos estados inicial y final
            inicio = Estado(estados)
            estados += 1
            fin = Estado(estados)
            estados += 1

            # # Crear transición desde el estado inicial al estado final con el caracter actual.
            trans = Transiciones(inicio, caracter, fin)
            
            # # Crear el nuevo autómata y apilarlo en el stack
            nuevo_automata = Automata(inicio, fin)
            
            # print(nuevo_automata.get_estado_inicial())
            # print(nuevo_automata.get_estado_final())
            
            # Guardando las transiciones de la forma (estado_inicial, caracter, estado_final) en un diccionario.
            stack.append(nuevo_automata)

            # Agregando los nuevos estados a la lista de estados.
            lista.append(trans)

    for automata in lista:
        print(str(automata))

    # # Imprimedo el inicio y el final del autómata.
    # print("Estado inicial: " + str(stack[0].get_estado_inicial()))
    # print("Estado final: " + str(stack[0].get_estado_final()))

    # Convirtiendo la lista de transiciones en un diccionario.
    for i in lista:
        if i.getEstadoInicial() in diccionario:
            diccionario[i.getEstadoInicial()].append((i.getSimbolo(), i.getEstadoFinal()))
        else:
            diccionario[i.getEstadoInicial()] = [(i.getSimbolo(), i.getEstadoFinal())]

    for key, value in diccionario.items():
        print(key, str(value))

    return lista

def graficar(lista): #Método para graficar el autómata.
    
    # Crea una nueva figura
    fig, ax = plt.subplots()

    # Dibuja el estado inicial como un círculo
    ax.add_patch(plt.Circle((0, 0), 0.1, color='black', fill=False))

    # Dibuja el estado final como un doble círculo
    ax.add_patch(plt.Circle((1, 0), 0.1, color='black', fill=False))
    ax.add_patch(plt.Circle((1, 0), 0.05, color='black'))

    # Dibuja la flecha que conecta los estados
    ax.arrow(0.1, 0, 0.8, 0, head_width=0.05, head_length=0.1, fc='black', ec='black')

    # Agrega etiquetas de texto a los estados y la transición
    ax.text(0, -0.2, 'Inicio', ha='center', va='top')
    ax.text(1, -0.2, 'Fin', ha='center', va='top')
    ax.text(0.5, 0.1, 'a', ha='center', va='bottom')

    # Configura los límites del gráfico y oculta los ejes
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 0.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Muestra el gráfico
    plt.show()

