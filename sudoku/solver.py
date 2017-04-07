from sudoku import Board

class Solver(Board):

    def __init__(self):
        super(Solver, self).__init__()

    def solve(self, row, col):
        i = self.cells[row][col]


fd = open('sudoku.txt')
fd.readline()
fd.readline()
p = fd.readline()
b = Solver()
b.setup(p)
for i in range(5):
    print (b.solve(0, 0))
