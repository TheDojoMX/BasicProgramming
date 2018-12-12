# Primeras dos letras de apellido paterno
# Primera lertra del materno
# Primera letra del nombre
# últimos dos deigitos del año de nacimiento
# dos digitos del mes de nacimiento
# dos dígitos del dia de nacimiento
# H para hombre / M para mujer
# Clave del estado de nacimiento
# Primera consonante interna del apellido paterno
# Primera consonante interna del apellido materno
# Primera consonante interna del nombre
# dos dígitos random -> 




def primera_consonante_interna(cadena):
    # Lista de consonantes
    consonantes = ['B', 'C', 'D' 'F']
    # LUNA
    for letra in cadena[1:]: # UNA
        if letra in consonantes:




def curp(apellido_paterno, apellido_materno,
    primer_nombre, anio, mes, dia, sexo,
    estado_nacimiento):
    res = ''
    res += apellido_paterno[0:2]
    res += apellido_materno[0]
    res += primer_nombre[0]
    res += anio[2:]
    res += mes
    res += dia
    res += sexo
    res += estado_nacimiento
    return res.upper()
print(
    curp("Patrcio","Moreno", "Héctor", '1989', '08', '12',
    'H', 'DF')
)