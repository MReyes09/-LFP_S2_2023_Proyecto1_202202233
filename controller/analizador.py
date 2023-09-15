class Analizador():

    def __init__(self, texto):
        self.texto = texto

    """
        Token válidos
            {
            }
            [
            ]
            strings --> Lo que sea menos un salto de linea
            decimales
            enteros ---> 0 - 9
            coma ------> ,
            dos puntos ---> :
        
        Estados: S0, S1, S2, S3
        S0 inicio
        Estados de aceptacion: S1, S3, S4
        
        S0 { } [ ] , : ------> S1
            "   ---> S2
            0-9   ------> S3
        
        S2 (Cualquier cosa) ---> S2
        S2 " -------------> S1
        
        S3 (0-9) ----------> S3
        S3 . ----------> S4
        
        S4 (0-9) -------> S5
        
        S5 (0-9) --------> S5
        
    """
    def analizar(self):
        fila = 1
        columna = 1
        estado = 0
        lexema = ""
        tokens_reconocidos = []

        for caracter in self.texto:

            ascii = ord(caracter)

            if estado == 0:

                if ascii == 34:#"

                    lexema += caracter

                    estado = 2

                elif caracter.isDigit(): #0-9 self.isNumero(ascii)

                    lexema += caracter
                    estado = 2

                elif self.simboloValido(ascii): #{ } [ ] , :

                    lexema += caracter
                    estado = 1

                else:

                    if ascii == 32 or ascii == 9 or ascii == 10:

                        pass

                    else:
                        pass

                    lexema = ""




    def isNumero(self, ascii):

        if ascii > 47 and ascii < 57:

            return True
        else:

            False

    def simboloValido(self, ascii):

        if ascii == 123 or ascii == 125 or ascii == 91 or ascii == 93 or ascii == 44 or ascii == 58:
            return True
        else:
            return False
