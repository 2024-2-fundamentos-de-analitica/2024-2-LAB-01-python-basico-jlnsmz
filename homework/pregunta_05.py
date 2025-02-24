"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
   
    lista = []
    resultado = {}
    lista_resultado = []
    with open("files/input/data.csv", "r") as file:
        data = file.readlines()
    
    for row in data:
        row = row.strip().split('\t')
        lista.append((row[0], int(row[1])))
        
    lista = sorted(lista, key = lambda x: (x[0], x[1]))
    
    # Recorrer la lista ordenada y obtener la primera y última tupla por letra
    for item in lista:
        letra = item[0]
        if letra not in resultado:
            # La primera tupla de esa letra
            resultado[letra] = [item[1], None]
        else:
            # Actualizar la última tupla de esa letra
            resultado[letra][1] = item[1]
            
    for key, value in resultado.items():
        lista_resultado.append((key, value[1], value[0]))
        
        
    return lista_resultado

#print(pregunta_05())