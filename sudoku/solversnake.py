from sudokusnake import Board

class Solver(object):

    def __init__(self):
        self.tablero = Board()

    def some(self, seq):
        for e in seq:
            if e: return e
        return False

    def solver(self, tablero, b):
        r = []
        r.append(tablero)
        while len(r) > 0:
            original = r.pop()
            if original.is_solved():
                self.tablero = original
                return True
            t = original.minimo()
            if t[0] == 0:
                continue
            for a in original.cells[t[1]][t[2]]:
                copia = Board()
                copia.setup_box(b)
                copia.setup(original.clone())
                copia.set_value(t[1], t[2], a)
                r.append(copia)
        return False

    def solve(self, b, p):
        self.tablero.setup_box(b)
        self.tablero.setup(p)
        print("Tablero Original")
        print(self.tablero)
        print("Forma del tablero")
        for i in self.tablero.get_box():
            print(i)
        if self.solver(self.tablero, b):
            print("Solucion")
            print(self.tablero)
        else:
            print('No hay Solucion')

fd = open('sudoku2.txt')
fd.readline()
fd.readline()
b = fd.readline()
print(b)
p = fd.readline()
print(p)
s = Solver()
s.solve(b, p)
