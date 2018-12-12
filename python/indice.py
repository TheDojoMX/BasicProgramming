# agencias = [
#     {
#         "nombre": "agencia1",
#         "skills": ["skill1"],
#     },
#     {
#         "nombre": "agencia2",
#         "skills": ["skill2"]
#     }
# ]


# indice = {
#     "skill1": ["agencia1", "agencia3"],
#     "skill2": ["agencia5", "agencia2"]
# }


# indice["skill2"]

from pprint import pprint
agencias = [
    {
        "nombre": "HAL",
        "skills": ["1", "2", "3"],
    },
    {
        "nombre": "BNN",
        "skills": ["1", "4", "5"],
    },
    {
        "nombre": "IAB",
        "skills": ["3", "5", "6"],
    },
]

def indexar(agencias):
    indice = {} # diccionario vacio
    for a in agencias:
        habilidades = a.get("skills")
        for h in habilidades:
            # verificar si el skill está en el diccionario
            agencias_skill = indice.get(h)
            if agencias_skill == None:
                # si no está, crear lista nueva con el nombre de la agencia
                indice[h] = []
            indice[h].append(a["nombre"])
    return indice
pprint(indexar(agencias))
