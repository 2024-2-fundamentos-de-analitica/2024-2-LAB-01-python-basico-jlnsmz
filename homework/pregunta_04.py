"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    
    fechas = []
    mes = []
    resultado = {}
    resultado_final = []
    with open("files/input/data.csv", "r") as file:
        data = file.readlines()
    
    for row in data:
        row = row.strip().split('\t')
        fechas.append(row[2].split('-'))
    
            
    for fecha in fechas:
        mes.append((fecha[1], 1))
    
    mes = sorted(mes, key = lambda x: x[0])
    
    for key, value in mes:
        if key not in resultado.keys():
            resultado[key] = 0
        resultado[key] += value
        
    for clave, valor in resultado.items():
        resultado_final.append((clave, valor))

            
    return resultado_final


#print(pregunta_04())


        
    
        