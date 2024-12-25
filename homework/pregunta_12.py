"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd


def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.

    Rta/
         c0                                   c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    # tabla_0 = "files/input/tbl0.tsv"
    # tabla_1 = "files/input/tbl1.tsv"
    tabla_2 = "files/input/tbl2.tsv"

    data = pd.read_csv(tabla_2, sep="\t")

    data["c5"] = data["c5a"].astype(str) + ":" + data["c5b"].astype(str)
    out = (
        data.groupby("c0")["c5"]
        .apply(lambda x: ",".join(map(str, sorted(x))))
        .reset_index()
    )

    return out


print(pregunta_12())
