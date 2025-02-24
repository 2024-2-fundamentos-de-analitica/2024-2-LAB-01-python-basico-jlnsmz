"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
  
    resultado = []
    dic = {}

    with open("files/input/data.csv", "r") as file:
        data = file.readlines()

    for row in data:
        row.split('\t')
        resultado.append((row[0], 1))
            
    resultado = sorted(resultado, key = lambda x: x[0])
    
    for key, value in resultado: 
        if key not in dic.keys():
            dic[key] = 0
        dic[key] += value
        
    result = list(dic.items())

    return result

#print(pregunta_02())
