# Calculadora
#
# Una sencilla calculadora que utilizara un parser descendente.
 #
 import re
 from sly.lex import lex
 from ast import *

 #_____________________________________________________________________
 # Simbolos

class Scanner(object):
	tokens = [ 
		'NUMBERS', 'ID', 'ASSIGN', 'PLUS',
		'MINUS', 'TIMES', 'DIVIDE', 'LPARENT',
		'RPARENT', 'SEMI'
	]
	t_ignore = '\t\n'
	t_NUMBER = r'\d+'
	t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
	t_ASSIGN = r'='
	t_PLUS = r'\+'
	t_MINUS = r'-'
	t_TIMES = r'\*'
	t_DIVIDE = r'/'
	t_LPARENT = r'\('
	t_RPARENT = r'\)'
	t_SEMI = r';'
	
	lexer = lex()

	def t_error(self, t):
		print('Entrada erronea %r' % t.value[0])
		t.lexer.skip(1)

#______________________________________________________________________
# Analizador descendente:

class Parser(object):
	def assigment(self):
		if self._accept("ID"):
			''' ID = expression '''
			name = self.tok.value
			self,_expect('ASSIGN')
			expr = self.expression()
			self._expect('SEMI')
			return Assigment(name, expr)
		else:
			raise SystaxError('Se esperaba un ID')

	def expression(self):
		''' expression : term (('+' | '-') term)  esta en forma bajus node'''
		expr = self.term()
		while self._expect('PLUS') or self._expect('MINUS'):
			operator = self.tok.value
			rigth = self.term()
			expr = BinOp(operator, expr, rigth)
		return expr

	def term(self):
		''' term: factor { ('*' | '/') factor}  en forma bajus node '''
		term = self.factor()
		while self._expect('TIMES') or self._expect('DIVIDE'):
			operator = self.tok.value
			rigth = self.factor()
			term = BinOp(operator, term, rigth)
		return term

	def factor(self):
		''' factor : ID | NUMBER | ( expression ) '''
		if self._accept('ID'):
			return Identifier(self.tok.value)
		elif self._accept('NUMBER'):
			return nUMBER(self.tok.value)
		elif self._accept('LPARENT'):
			expr = self.expression()
			self._expect('RPARENT')
			return expr
		else:
			raise SystaxError('Se esperaba ID, NUMBER o LPARENT')
