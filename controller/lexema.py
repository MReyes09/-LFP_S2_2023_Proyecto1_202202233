from template.operador import Operador


class Lexema(Operador):

    def __init__(self, lexema, f, c):
        self.lexema = lexema
        super().__init__(f, c)

    def operar(self, tree):

        return self.lexema

    def get_F(self):

        return super().get_F()

    def get_C(self):

        return super().get_C()
