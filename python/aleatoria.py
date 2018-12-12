import random
lista_alumnos = ["Nadia", "Rocío", "Valeria", "Ángel", "Frank", "Iván"]

# Comprobando que los tres sean iguales
count = 0
while True:
    alumno1 = random.choice(lista_alumnos)
    alumno2 = random.choice(lista_alumnos)
    alumno3 = random.choice(lista_alumnos)
    count += 1
    if alumno1 == alumno2 and alumno2 == alumno3:
        print("El ganador es: {}".format(alumno1))
        print("Encontrado después de : {} iteraciones".format(count))
        break
