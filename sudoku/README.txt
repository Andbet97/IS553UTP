Proyecto Sudoku

Para el primer punto del proyecto se quiere resolver un sudoku de 9x9 con la ayuda
del patron observador, como sugerencia y tema principal se utilizara backtracking.

El archivo "sudoku.py" junto con "solver.py" soluciona dicho punto:
  Se utiliza una lista para simular una pila, dicha pila se encarga de guardar
  copias de los tableros con un valor asignado en la casilla que tenga menor
  número de posibilidades, dichos valor entonces es uno de los posibles valores
  de la casilla.

Para el segundo punto se propone resolver sudokus serpiente, es decir sudokus
irregulares.

El archivo "sudokusnake.py" junto con "solversnake.py":
  En este archivo se cambia la forma de ingresar el sudoku, dando la forma primero
  y los valores en una segunda linea, asi se tiene como ejemplo que si se quiere
  resolver un sudoku con forma regular la entrada seria de esta forma:
    111222333111222333111222333444555666444555666444555666777888999777888999777888999
    53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79

    que representa:
    +---------+---------+---------+
    | 5  3  4 | 6  7  8 | 9  1  2 |
    | 6  7  2 | 1  9  5 | 3  4  8 |
    | 1  9  8 | 3  4  2 | 5  6  7 |
    +---------+---------+---------+
    | 8  5  9 | 7  6  1 | 4  2  3 |
    | 4  2  6 | 8  5  3 | 7  9  1 |
    | 7  1  3 | 9  2  4 | 8  5  6 |
    +---------+---------+---------+
    | 9  6  1 | 5  3  7 | 2  8  4 |
    | 2  8  7 | 4  1  9 | 6  3  5 |
    | 3  4  5 | 2  8  6 | 1  7  9 |
    +---------+---------+---------+
  esta seria la unica diferencia entre los dos solver que existen, su
  funcionamiento es exactamente el mismo.
