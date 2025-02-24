"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    
    lista = []
    dic = {}
    resultado_final = []
    with open("files/input/data.csv", "r") as file:
        data = file.readlines()
    
    for row in data:
        row = row.strip().split('\t')
        lista.append((row[0],int(row[1])))
        
    lista = sorted(lista, key = lambda x: x[1])
    
    for value, key in lista:
        if key not in dic:
            dic[key] = []
        dic[key].append(value)
    
    for clave, valor in dic.items():
        resultado_final.append((clave, valor))
        
    return resultado_final

#print(pregunta_07())
