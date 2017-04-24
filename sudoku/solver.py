from sudoku import Board
from copy import deepcopy

class Solver(Board):

    def __init__(self):
        super(Solver, self).__init__()

    def is_solved(self, tablero):
        for i in range(9):
            for j in range(9):
                if not tablero.cells[i][j].is_solved:
                    return False
        return True

    def some(self, tablero):
        for i in tablero:
            if i:
                return i
        return False

    def solver(self, tablero):
        row = 0
        col = 0
        mini = 10
        if tablero is False:
            return False
        if self.is_solved(tablero):
            self.tablero = tablero
            return True
        for i in range(9):
            for j in range(9):
                if tablero.cells[i][j].len() > 1 and tablero.cells[i][j].len() < mini :
                  row = i
                  col = j
        copia = deepcopy(tablero)
        return self.some(self.solver(copia.cells[row][col].set_value(d)) for d in tablero.cells[row][col])

    def solve(self, p):
        self.setup(p)
        copia = deepcopy(self.cells)
        if self.solver(copia):
            print(self)
        else:
            print('No hay Solucion')

fd = open('sudoku.txt')
fd.readline()
fd.readline()
p = fd.readline()
b = Solver()
b.solve(p)
