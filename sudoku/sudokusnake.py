# coding: utf-8
from observable  import Observable
from wrapt import synchronized
import math

class Cell(Observable):

	def __init__(self, row, col):
		super(Cell, self).__init__()
		self.values = [i+1 for i in range(9)]
		self.is_solved = False
		self.row = row
		self.col = col

	def __iter__(self):
		for val in self.values:
			yield val

	def __len__(self):
		return len(self.values)

	def set_value(self, value):
		self.values = [value]
		self.is_solved = True
		self.notify_observers(value)

	def get_value(self):
		return self.values[0] if self.is_solved else 0

	def add_observer(self, cells, box):
		N = len(cells)
		for i in range(N):
			for j in range(N):
				if i == self.row and j == self.col: continue
				is_sline = (i == self.row) or (j == self.col)
				is_sbox  = box[self.row][self.col] == box[i][j]
				if is_sline or is_sbox:
					#if self.row == self.col == 5:
					#	print(self.row, self.col, i, j)
					super(Cell, self).add_observer(cells[i][j])

	@synchronized
	def update(self, value):
		if self.is_solved or value == 0: return
		#if self.row == 5 and self.col == 5:
		#	print(value, self.values)
		if value in self.values: self.values.remove(value)
		#if not self.is_solved and len(self.values) == 1:
			#self.set_value(self.values[0])

'''
Representa el tablero del Sudoku
'''
class Board(object):

    def __init__(self, N = 9):
        self.box = []
        self.cells = [[Cell(i,j) for j in range(N)] for i in range(N)]
        # Adiciona observadores

    def __len__(self):
        return len(self.cells)

    def __str__(self):
        N = len(self)
        str = ''
        for i in range(N):
            for j in range(N):
                value = self.cells[i][j].get_value()
                str += ' {} '.format(value if value != 0 else '.')
            str += '\n'
        return str

    def get_box(self):
        return self.box    

    def setup(self, puzzle):
        N = len(self)
        if isinstance(puzzle, list):
            self._setup_from_list(puzzle)
        elif isinstance(puzzle, str):
            self._setup_from_str(puzzle)

    def _setup_from_list(self, puzzle):
        N = len(self)
        assert len(puzzle) == N
        for i in range(N):
            for j in range(N):
                if puzzle[i][j] == 0: continue
                self.cells[i][j].set_value(puzzle[i][j])

    def _setup_from_str(self, puzzle):
        N = len(self)
        #assert math.sqrt(len(puzzle)) == N
        for i in range(N):
            for j in range(N):
                c = puzzle[i*N+j]
                if c == '.': continue
                self.cells[i][j].set_value(int(c))

    def setup_box(self, puzzle):
        N = len(self)
        if isinstance(puzzle, list):
            self._setup_box_from_list(puzzle)
        elif isinstance(puzzle, str):
            self._setup_box_from_str(puzzle)
        for i in range(N):
            for j in range(N):
                self.cells[i][j].add_observer(self.cells, self.box)

    def _setup_box_from_list(self, puzzle):
        N = len(self)
        assert len(puzzle) == N
        for i in range(N):
            self.box.append([])
            for j in range(N):
                self.box[i].append(puzzle[i][j])

    def _setup_box_from_str(self, puzzle):
        N = len(self)
        #assert math.sqrt(len(puzzle)) == N
        for i in range(N):
            self.box.append([])
            for j in range(N):
                c = puzzle[i*N+j]
                self.box[i].append(int(c))

    def set_value(self, row, col, value):
        self.cells[row][col].set_value(value)

    def clone(self):
        N = 9
        new = []
        for i in range(N):
            new.append([])
            for j in range(N):
                new[i].append(self.cells[i][j].get_value())
        return new

    def is_solved(self):
        for i in range(9):
            for j in range(9):
                if not self.cells[i][j].is_solved:
                    return False
        return True

    def minimo(self):
        r = []
        mini = 10
        for row in range(9):
            for col in range(9):
                if (len(self.cells[row][col]) < mini and
                not self.cells[row][col].is_solved):
                    mini = len(self.cells[row][col])
                    r = [mini, row, col]
        return r

#fd = open('sudoku.txt')
#fd.readline()
#fd.readline()
#fd.readline()
#p = fd.readline()
#b = Board()
#b.setup(p)
#print(b)
