from template.operador import Operador


class Aritmetica(Operador):

    def __init__(self, izquierdo, derecho, tipo, f, c):
        self.i = izquierdo
        self.d = derecho
        self.t = tipo
        super().__init__(f, c)

    def operar(self, tree):

        i_valor = ''
        d_valor = ''

        if self.i is not None:

            i_valor = self.i.operar(tree)

        if self.d is not None:

            d_valor = self.d.operar(tree)

        if self.t.operar(tree) == "suma":

            return i_valor + d_valor

        elif self.t.operar(tree) == "resta":

            return i_valor - d_valor

        elif self.t.operar(tree) == "multiplicacion":

            return i_valor * d_valor

        elif self.t.operar(tree) == "division":

            return i_valor / d_valor

        elif self.t.operar(tree) == "mod":

            return i_valor % d_valor

        elif self.t.operar(tree) == "potencia":

            return i_valor ** d_valor

        elif self.t.operar(tree) == "raiz":

            return i_valor ** (1 / d_valor)

        elif self.t.operar(tree) == "inverso":

            return 1 / i_valor

        else:

            return None

    def get_F(self):

        return super().get_F()

    def get_C(self):

        return super().get_C()