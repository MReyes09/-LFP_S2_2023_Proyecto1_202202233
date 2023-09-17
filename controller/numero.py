
from template.operador import Operador

class Numero(Operador):

    def __init__(self, numero, f, c):
        self.n = numero
        super().__init__(f, c)

    def operar(self, tree):

        return self.n

    def get_F(self):

        return super().get_F()

    def get_C(self):

        return super().get_C()