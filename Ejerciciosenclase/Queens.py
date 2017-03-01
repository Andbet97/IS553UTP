
N = 8


class Queen:

	def __init__(self,col,neighbor):
		self.row = 1
		self.col = col
		self.neighbor = neighbor

	def find_solution(self):
		while self.neighbor is not None and self.neighbor.can_attack(self.row,self.col):
			if not self.advance():
				return False
		return True

	def advance(self):
		if self.row < N:
			self.row += 1
			return self.find_solution()
		if not self.neighbor.advance(): return False
		self.row = 1
		return self.find_solution()


	def qprint(self):
		if self.neighbor is not None:
			self.neighbor.qprint()
		print (self.row , self.col)

	def can_attack(self,row,col):
		# probar misma fila
		if self.row == row:
			return True
		# probar diagonales
		diff = col - self.col
		if self.row +diff == row or self.row - diff == row:
			return True
		#no se puede atacar depronto el vecino puede
		return self.neighbor is not None and self.neighbor.can_attack(row,col)



if __name__ == '__main__':
		q = None
		for i in range(N):
			q = Queen(i+1,q)
			if not q.find_solution():
				print ("sin solucion")
		q.qprint()

#hacer la animacion con graphics.py
