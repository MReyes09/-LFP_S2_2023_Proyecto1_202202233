from abc import ABC, abstractmethod

class Operador(ABC):

    def __init__(self, f, c):
        self.f = f
        self.c = c

    @abstractmethod
    def operar(self, tree):

        pass

    @abstractmethod
    def get_F(self):

        return self.f

    @abstractmethod
    def get_C(self):

        return self.c