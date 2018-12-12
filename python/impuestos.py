
# 16%
def iva(precio):
    """
    Calcula el IVA considerando un 16%
    """
    return precio * 0.16

def esta_entre(cantidad, inf=0, sup=10000):
    """
    Verifica si una cantidad está entre un rango
    """
    return cantidad > inf and cantidad <= sup

# esta_entre(5000, 4000, 6000)

def isr(cantidad):
    """
    Calcula el ISR basado en la tabla de ingresos
    """
    if esta_entre(cantidad, inf=5000, sup=10000):
        tasa = 0.25
    elif esta_entre(cantidad, 10000, 100000):
        tasa = 0.30
    elif cantidad > 100000:
        tasa = 0.35
    else:
        tasa = 0

    return cantidad * tasa

def imss(cantidad, edad):
    """
    Calcula lo que se le paga al IMSS basado en el seguro
    """
    if esta_entre(edad, 20, 30):
        tasa = 0.25
    elif esta_entre(edad, 30, 50):
        tasa = 0.3
    elif edad > 50:
        tasa = 0.35
    return cantidad * tasa


print(isr(100001))
print(imss(1000, 50))
