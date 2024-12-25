"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    # tabla_0 = "files/input/tbl0.tsv"
    tabla_1 = "files/input/tbl1.tsv"
    # tabla_2 = "files/input/tbl2.tsv"

    data = pd.read_csv(tabla_1, sep="\t")
    value = sorted(data["c4"].unique())

    out = [valor.upper() for valor in value]

    return out
