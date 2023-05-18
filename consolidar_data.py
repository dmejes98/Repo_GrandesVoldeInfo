# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 16:40:16 2023

@author: David Mejia
"""

import pandas as pd
import numpy as np
import time
import os

inicio = time.time()
# Nombre de la carpeta que contiene los archivos de Excel
nombre_carpeta = "SEN"  

# Obtener la ruta completa de la carpeta
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_carpeta = os.path.join(ruta_actual, nombre_carpeta)

archivos = os.listdir(ruta_carpeta)

operaciones = pd.DataFrame(columns=[])

    
archivos_excel = [archivo for archivo in archivos if archivo.endswith((".xlsx", ".xls"))]


for elemento in archivos_excel:
    ruta_archivo = os.path.join(ruta_carpeta, elemento)
    libro = pd.read_excel(ruta_archivo, header=[9])
    
    print(elemento)
    # Retiramos TUVT
    aux = []
    for i in libro.index:

        aux.append(libro.iloc[i, 4][0:4])

    del i

    libro["aux"] = aux

    libro = libro[libro["aux"] != ("TFVT")]

    # Retiramos Operaciones de Liquidez
    libro = libro[libro["SESION/RUEDA"] == "CONH"]


    operaciones = pd.concat([operaciones, libro])
    print(elemento)

operaciones.columns
operaciones.drop(
    [
        "aux",
        "* VR. NOMINAL COLATERAL",
        "PLAZO (De regreso para SIML, Repos e INTB)",
        "* TASA/ PRECIO\nCOLATERAL",
        "* TASA/ PRECIO\nEQUIV.\nCOLATERAL",
    ],
    axis=1,
    inplace=True,
)


operaciones.reset_index(inplace=True)
operaciones.drop(["index"], axis=1, inplace=True)

final = time.time()

ejec_time = (final - inicio) / 60
print("Tiempo de ejecución en minutos: ", ejec_time)


operaciones['HORA DE CIERRE'] = operaciones['HORA DE CIERRE'].apply(lambda x: x.replace(":", "") if isinstance(x, str) else x)
operaciones.to_csv('SEN.csv')
