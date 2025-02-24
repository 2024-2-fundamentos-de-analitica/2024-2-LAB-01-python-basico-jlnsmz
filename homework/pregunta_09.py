"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    
    
    lista =[]
    tuplas = []
    resultado = {}
    with open("files/input/data.csv", "r") as file:
        data = file.readlines()
    
    for row in data:
        row = row.strip().split('\t')            
        aux = row[4].strip().split(',')
        
        for data in aux:
            lista.append(tuple(data.split(':')))
            
    
    for data in lista:
        tuplas.append((data[0],1))
    
    tuplas = sorted(tuplas, key = lambda x: x[0])
    
    for key, value in tuplas:
        if key not in resultado.keys():
            resultado[key] = 0
        resultado[key] += value
            
    return resultado
            
#print(pregunta_09())