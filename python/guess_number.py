# -*- coding: utf-8 -*-

# Computadora elige número aleatorio entre 0 y 100
# Pregunta al usuario por un número
# Si el número es igual, el juego termina
# El usuario tiene 5 intentos

import random

elegido = random.randint(0, 10)
intentos = 15
numero_usuario = ''

# undefined
# print(elegido)
while intentos > 0 and numero_usuario != elegido:
    numero_usuario = int(input("Escoge un número: "))
    # print(type(numero_usuario))
    if numero_usuario == elegido:
        print("GANASTE")
    else:
        intentos -= 1
        print("Fallaste, lo siento, te quedan {} oportunidades".format(intentos))




