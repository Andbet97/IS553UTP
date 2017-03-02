#creado por Angel Augusto Agudelo Zapata

import graphics


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
		x = (self.row-1)*50 + 25
		y = (self.col-1)*50 + 25
		reina = graphics.Circle(graphics.Point(x, y), 10)
		reina.setFill("black")
		reina.setOutline("black")
		reina.draw(win)

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
	print ("Ingrese el numero de reinas: ")
	N = input()
	win = graphics.GraphWin("8 Reinas", 400, 400)
	win.setBackground("white")
	#esta parte hace el tablero
	for c in range(N):
		for r in range(N):
			x = c*(400/N)
			y = r*(400/N)
			a = graphics.Rectangle(graphics.Point(x, y),
			                       graphics.Point(x+(400/N), y+(400/N)))
			if ((r-c)%2 == 0):
				a.setFill(graphics.color_rgb(238, 213, 183))
				a.setOutline(graphics.color_rgb(238, 213, 183))
			else:
				a.setFill(graphics.color_rgb(102, 51, 0))
			a.draw(win)
	q = None
	for i in range(N):
		q = Queen(i+1,q)
		if not q.find_solution():
			print ("sin solucion")
	q.qprint()
	win.getMouse() # Pause to view result
	win.close()    # Close window when done

#hacer la animacion con graphics.py
