# esto es para crear la funcion 
>>> def mod(a,b):
		ans = a%b
		return ans

# se mira que posee una direccion
>>> mod
# se ve que el codigo tambien es un objeto
>>> mod.func_code # 2.7
>>> mod.__code__ #3.5 adelante
# se ve la representacion hexadecimal del codigo del codigo
>>> mod.__code__.__code__
# lista de instrucciones
>>> [ord(b) for b in mod.__code__.__code__]
#importa dis
>>> import dis
# se ve el procedimiento interno del interprete
>>> dis.dis(mod)