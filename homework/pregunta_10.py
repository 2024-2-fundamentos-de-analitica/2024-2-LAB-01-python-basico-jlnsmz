"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    
    
    tuplas = []
    with open("files/input/data.csv", "r") as file:
        data = file.readlines()

    for row in data:
        row = row.strip().split('\t')
        col_4 = len(row[3].split(','))
        col_5 = len(row[4].strip().split(','))
        tuplas.append((row[0], col_4, col_5))
            
        

    return tuplas

#print(pregunta_10())

    
        
