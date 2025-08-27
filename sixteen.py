"""
Logica del juego Sixteen
"""

import random


def crear_tablero(n_filas: int, n_columnas: int) -> list[list[int]]:
    """
    Crea un tablero ordenado, con dimensiones `n_filas` por `n_columnas`.

    El tablero estará representado como una lista de listas de enteros. El
    primer número en la posición `[0][0]` será un 1, el de la izquierda será un
    2, y así sucesivamente hasta completar todos los casilleros, sin repetir
    los números, hasta llegar al número `n_filas * n_columnas`.

    PRECONDICIONES:
        - `n_filas` y `n_columnas` son enteros positivos mayor a uno y menores
        a diez.

    POSTCONDICIONES:
        - la función devuelve un nuevo tablero ordenado de enteros que se puede
        utilizar para llamar al resto de las funciones del módulo.

    EJEMPLO:
        >>> crear_tablero(4, 5)
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
        ]
    """
    tablero = []
    contador = 1

    for i in range(n_filas):
        fila = []
        for j in range(n_columnas):
            fila.append(contador)
            contador += 1
        tablero.append(fila)
        # print(fila, end="")
    return tablero

    # print(tablero)


# print(crear_tablero(3, 3))


def rotar_izquierda(tablero: list[list[int]], fila: int) -> bool:
    """Rota la fila del tablero, indicada por el índice `fila`, hacia la
    izquierda.

    Por ejemplo, con `fila=1` y `tablero` como a la izquierda, al finalizar
    la función se modificará el tablero para que quede como en la derecha.
    [[1, 2, 3],           [[1, 2, 3],
     [4, 5, 6],    ==>     [5, 6, 4],
     [7, 8, 9]]            [7, 8, 9]]

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.

    POSTCONDICIONES:
        - Si `fila` es un índice de filas válido, la función realiza la
        rotación modificando el tablero y devuelve `True`.
        Caso contrario, no modifica el tablero y devuelve `False`."""
    
    for fila in tablero:
        for i in fila:
            tablero[fila][-1] =  tablero[fila][i]





def rotar_derecha(tablero: list[list[int]], fila: int) -> bool:
    """Rota la fila del tablero, indicada por el índice `fila`, hacia la
    derecha.

    Por ejemplo, con `fila=1` y `tablero` como a la izquierda, al finalizar
    la función se modificará el tablero para que quede como en la derecha.
    [[1, 2, 3],           [[1, 2, 3],
     [4, 5, 6],    ==>     [6, 4, 5],
     [7, 8, 9]]            [7, 8, 9]]

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.

    POSTCONDICIONES:
        - Si `fila` es un índice de filas válido, la función realiza la
        rotación modificando el tablero y devuelve `True`.
        Caso contrario, no modifica el tablero y devuelve `False`."""


def rotar_arriba(tablero: list[list[int]], columna: int) -> bool:
    """Rota la columna del tablero, indicada por el índice `columna`, hacia
    arriba.

    Por ejemplo, con `columna=1` y `tablero` como a la izquierda, al finalizar
    la función se modificará el tablero para que quede como en la derecha.
    [[1, 2, 3],           [[1, 5, 3],
     [4, 5, 6],    ==>     [4, 8, 6],
     [7, 8, 9]]            [7, 2, 9]]

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.

    POSTCONDICIONES:
        - Si `columna` es un índice de columnas válido, la función realiza la
        rotación modificando el tablero y devuelve `True`.
        Caso contrario, no modifica el tablero y devuelve `False`."""


def rotar_abajo(tablero: list[list[int]], columna: int) -> bool:
    """Rota la columna del tablero, indicada por el índice `columna`, hacia
    abajo.

    Por ejemplo, con `columna=1` y `tablero` como a la izquierda, al finalizar
    la función se modificará el tablero para que quede como en la derecha.
    [[1, 2, 3],           [[1, 8, 3],
     [4, 5, 6],    ==>     [4, 2, 6],
     [7, 8, 9]]            [7, 5, 9]]

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.

    POSTCONDICIONES:
        - Si `columna` es un índice de columnas válido, la función realiza la
        rotación modificando el tablero y devuelve `True`.
        Caso contrario, no modifica el tablero y devuelve `False`."""


def esta_ordenado(tablero: list[list[int]]) -> bool:
    """
    Indica si los elementos del tablero se encuentran ordenados de izquierda a
    derecha, arriba a abajo, con el primer elemento siendo un 1 y cada elemento
    subsecuente incrementando su valor por uno.
    Por ejemplo, todo tablero que devuelva `crear_tablero` empieza ordenado.

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.
        - Los elementos de `tablero` no tienen números repetidos.
    """


def mezclar_tablero(tablero: list[list[int]]):
    """
    Realiza ITERACIONES_RANDOM movimientos aleatorios al juego, siendo un
    movimiento cualquiera de las cuatro rotaciones sobre cualquier índice
    respectivo.

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.
    """
