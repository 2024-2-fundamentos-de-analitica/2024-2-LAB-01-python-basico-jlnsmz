"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    lista =[]
    resultado = {}
    resultado_final = []
    with open("files/input/data.csv", "r") as file:
        data = file.readlines()
    
    for row in data:
        row = row.strip().split('\t')
        aux = row[4].strip().split(',')
        for data in aux:
            lista.append(tuple(data.split(':')))
    
    for key, value in lista:
        value = int(value)
        if key not in resultado:
            resultado[key] = [value, value]
        if value < resultado[key][0]:
            resultado[key][0] = value
        if value > resultado[key][1]:
            resultado[key][1] = value
            
    resultado = sorted(resultado.items())
    
    for clave, valor in resultado:
        resultado_final.append((clave,valor[0], valor[1]))
    

    return resultado_final


#print(pregunta_06())




        
    
        

        
        
        

        
    
    
