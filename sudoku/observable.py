# no se usara observer, si se usara observable
from abc import ABCMeta, abstractmethod #para definis clase abstracta

class Observer(object):
    """clase abstracta Observer."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

class Observable(object):
    """clase Observable."""

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def delete_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def delete_observers(self, observer):
        if self.observers:
            # del elimina [desde:hasta] los elementos de la lista
            del self.observers[:]

    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)
