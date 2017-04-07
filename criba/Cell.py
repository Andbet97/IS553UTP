class Cell(object):
    """docstring forCell."""
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.values = [i+1 for i in range(9)]
        self.is_solved = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.values == []:
            raise StopIteration
        else:
            a = self.values[0]
            self.values = self.values[1:]
            return a


if __name__ == '__main__':
    f = Cell(1,1)
    for i in f:
        print (i)
