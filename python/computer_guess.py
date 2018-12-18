def guess():
    inf_limit = 1
    sup_limit = 100
    response = "n"
    while response != "s":
        my_number = get_number(inf_limit, sup_limit)
        print("Tu número es: {}".format(my_number))
        response = input("¿Adiviné? (s/n)")
        if response != 's':
            up_or_down = input('¿Mayor o menor? (u/d)')
            if up_or_down == "u":
                inf_limit = my_number
            else:
                sup_limit = my_number
    else:
        print("¡Gané!")

def get_number(inf, sup):
    diff = sup - inf
    return inf + int(diff/2)


print("Juguemos a adivinar el número.\nPiensa en un número(1-100) y yo lo adivinaré en menos de 7 intentos.\n")
guess()