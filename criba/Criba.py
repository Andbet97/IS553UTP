class Criba(object):
    """Criba de eratosteles."""
    def __init__(self):
        self.criba = [i+2 for i in range(99)]
        for i in self.criba:
            if i*i > 100:
                break
            for a in self.criba:
                if a > i and a%i == 0:
                    self.criba.remove(a)

    def generate(self):
        aux = [d+self.criba[-1]+1 for d in range(100)]
        for i in self.criba:
            for a in aux:
                if a%i == 0:
                    aux.remove(a)
        for i in aux:
            for a in aux:
                if a > i and a%i == 0:
                    aux.remove(a)
        for i in aux:
            self.criba.append(i)

    def __iter__(self):
        for i in self.criba:
            if i == self.criba[-1]:
                self.generate()
            yield i

class Primo(object):

    def __init__(self):
        self.n = 0
        self.lista = []
        self.criba = Criba()

    def give(self, n):
        self.lista = []
        self.n = n

    def __iter__(self):
        a = 0
        for i in self.criba:
            a += 1
            if a == self.n+1:
                break
            self.lista.append(i)
        yield self.lista

if __name__ == '__main__':
    f = Primo()
    f.give(30)
    for i in f:
        print(i)
    f.give(2)
    for i in f:
        print(i)

    #print (f.give(10))
