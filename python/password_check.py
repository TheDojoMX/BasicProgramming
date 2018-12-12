
password = "hellodave"

# Condiciones
# if len(password) <= 10:
#     print("Tu password no funciona")

# Mayusculas
tiene_mayusculas = False
for char in password:
    if char.isupper():
        tiene_mayusculas = True

special_chars = ['.', ',', ';', ':', '*', '@', '%', '/']


tiene_car_esp = False
for c in password:
    if c in special_chars:
        tiene_car_esp = True
        break

print("Tiene mayúsculas: {}".format(tiene_mayusculas))
