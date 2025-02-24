"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    
   
    lista = []
    col_1 = []
    dicc = {}
                

    with open("files/input/data.csv", "r") as file:
        data = file.readlines()
    
    for row in data:
        row = row.strip().split('\t')
        col_1.append(row[0])
        aux = row[4].strip().replace(',', ':').split(':')
        suma = 0
        for i in range(len(aux)):
            if i%2 != 0:
                suma+= int(aux[i])
        lista.append(suma)
        
        
    for letra, sum in zip(col_1, lista):
        if letra not in dicc.keys():
            dicc[letra] = 0
        dicc[letra] += sum
    
    keys = dicc.keys()
    
    result = dict(sorted(dicc.items()))
        
            
    return result

#print(pregunta_12())


        
    
    
        