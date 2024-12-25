"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd


def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    tabla_0 = "files/input/tbl0.tsv"
    # tabla_1 = "files/input/tbl1.tsv"
    tabla_2 = "files/input/tbl2.tsv"

    tbl_0 = pd.read_csv(tabla_0, sep="\t")
    tbl_2 = pd.read_csv(tabla_2, sep="\t")

    data = pd.merge(tbl_0, tbl_2, on="c0")

    out = data.groupby("c1")["c5b"].sum()

    return out


print(pregunta_13())
