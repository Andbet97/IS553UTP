class AST(object):
    '''
    Clase base para todos los nodos del AST.
    En cada nodo se espera definir el atributo _fields, el cual,
    enumera los nombres de los atributos almacenados.
    El método a continuación, __init__(), toma argumentos posicionales
    y los asigna a los campos apropoados.  Cualquier argumento
    adicional, especificado como kwargs, son tambien asignados
    
    '''
    _fields = []

    def __init__(self, *args, **kwargs):
        assert len(args) == len(self._fields)
        for name,value in zip(self._fields, args):
            setattr(self, name, value)
            
        # Asigna argumentos adicionales (keywords), si se sumunistran
        for name,value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        return self.__class__.__name__

    def pprint(self):
        for depth, node in flatten(self):
            print('%s%s' % (' '*(2*depth), node))

def validate_fields(**fields):
    def validator(cls):
        old_init = cls.__init__
        def __init__(self, *args, **kwargs):
            old_init(self, *args, **kwargs)
            for field,expect_type in fields.items():
                assert isinstance(getattr(self, field), expect_type)
        cls.__init__ = __init__
        return cls
    return validator

class NodeVisitor(object):
    '''
    '''

    def visit(self, node):
        '''
        Ejecuta un método de la forma visit_NodeName(node), donde NodeName
        es el nombre de la clase de un nodo en particular
        '''
        if node:
            method = 'visit_' + node.__class__.__name__
            visitor = getattr(self, method, self.generic_visit)
            return visitor(node)
        else:
            return None

    def generic_visit(self, node):
        '''
        Metodo ejecutado si no se encuentra el metodo aplicable visit_.
        Este examina al nodo para saber si tiene _fields es una lista o
        puede ser recorrido completamente.
        '''
        for field in getattr(node, '_fields'):
            value = getattr(node, field, None)
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, AST):
                        self.visit(item)
            elif isinstance(value, AST):
                self.visit(value)

def flatten(top):
    '''
    Aplana el arbol de sintaxis dentro de una lista para efectos
    de depuracion y pruebas.
    Este retorna una lista de tuplas de forma (depth, node) donde
    depth es un entero representando la profundidad del arbol y
    node es un nodo de AST.
    '''
    class Flattener(NodeVisitor):
        
        def __init__(self):
            self.depth = 0
            self.nodes = []

        def generic_visit(self, node):
            self.nodes.append((self.depth, node))
            self.depth += 1
            NodeVisitor.generic_visit(self, node)
            self.depth += 1

    d = Flattener()
    d.visit(top)
    return d.nodes


class Number(AST):
    _fields = ['value']

class BinOp(AST):
    _fields = ['left','right','op']


top = BinOp(BinOp(Number(1), BinOp(Number(2), Number(3), '*'), '+'), BinOp(Number(4), Number(5), '/'), '-')

class Calc(NodeVisitor):

    def visit_Number(self, node):
        return node.value

    def visit_BinOp(self, node):
        left  = self.visit(node.left)
        right = self.visit(node.right)
        if node.op == '+':
            return left + right
        elif node.op == '-':
            return left - right
        elif node.op == '*':
            return left * right
        elif node.op == '/':
            return left / right
        return None

calc = Calc()
print calc.visit(top)







