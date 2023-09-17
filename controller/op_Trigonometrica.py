from template.operador import Operador
import math as o

class Trigonometrica(Operador):

    def __init__(self, izquierdo, tipo, f, c):
        self.i = izquierdo
        self.t = tipo
        super().__init__(f, c)

    def operar(self, tree):

        i_valor = ''

        if self.i is not None:

            i_valor = o.radians(self.i.operar(tree))

        if self.t.operar(tree) == "seno":

            return o.sin(i_valor)

        elif self.t.operar(tree) == "coseno":

            return o.cos(i_valor)

        elif self.t.operar(tree) == "tangente":

            return o.tan(i_valor)

        else:

            return None

    def get_F(self):

        return super().get_F()

    def get_C(self):

        return super().get_C()