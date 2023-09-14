class Error():

    def __init__(self, lexema, tipo, columna, fila):
        self.lexema = lexema
        self.tipo = tipo
        self.col = columna
        self.fil = fila