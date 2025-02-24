"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
     
    lista = []
    resultado = {}
    with open("files/input/data.csv", "r") as file:
        data = file.readlines()

    for row in data:
        row.split('\t')
        lista.append((row[0], int(row[2])))
        
    lista = sorted(lista, key = lambda x: x[0])
    
    for key, value in lista:
        if key not in resultado.keys():
            resultado[key] = 0
        resultado[key] += value
    result = list(resultado.items())
    return result

#print(pregunta_03())