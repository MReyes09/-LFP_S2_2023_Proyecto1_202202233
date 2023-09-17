from controller.op_Aritmetica import *
from controller.op_Trigonometrica import *
from controller.lexema import *
from controller.numero import *


class Analizador():

    def __init__(self, texto):
        self.texto = texto
        self.f = 1
        self.c = 1
        self.tokens = []
        self.lexemas_List = []
        self.accion = []

    def generate_Lexemas_List(self):

        word_Reserved = {
            # VALORES
            'ROperacion': 'operacion',
            'RValor1': 'valor1',
            'RValor2': 'valor2',

            # OPERADORES
            'RSuma': 'suma',
            'RResta': 'resta',
            'RMultiplicacion': 'multiplicacion',
            'RDivision': 'division',
            'RPotencia': 'potencia',
            'RRaiz': 'raiz',
            'RInverso': 'inverso',
            'RSeno': 'seno',
            'RCoseno': 'coseno',
            'RTangente': 'tangente',
            'RMod': 'mod',

            # CONFIGURACIONES
            'RTexto': 'texto',
            'RFondo': 'fondo',
            'RFuente': 'fuente',
            'RForma': 'forma',

            # CARACTERES ESPECIALES
            'Coma': ',',
            'Punto': '.',
            '2Punts': ':',
            'CorI': '[',
            'CorD': ']',
            'LlaveI': '{',
            'LLaveD': '}',
        }

        self.lexemas_List = list(word_Reserved.values())

    def analizar(self):
        f = self.f
        c = self.c
        tokens = self.tokens
        cadena = self.texto
        lexema = ""
        puntero = 0

        while cadena:

            caracter = cadena[puntero]
            puntero += 1
            ascii = ord(caracter)

            if ascii == 34:
                # concateno todo lo que hay en " "
                lexema, cadena = self.find_Str(cadena[puntero:])

                if lexema and cadena:
                    lex = Lexema(lexema, f, c)
                    c += 1
                    tokens.append(lex)
                    c += len(lexema) + 1
                    puntero = 0

            elif caracter.isdigit():

                token, cadena = self.find_Number(cadena)

                if token and cadena:
                    num = Numero(token, f, c)
                    c += 1
                    tokens.append(num)
                    c += len(str(token)) + 1
                    puntero = 0

            elif ascii == 91 or ascii == 93:

                char = Lexema(lexema, f, c)
                tokens.append(char)
                c += 1
                cadena = cadena[1:]
                puntero = 0

            elif ascii == 9:

                c += 3
                cadena = cadena[3:]  # Se cortan los espacios de la tabulacion
                puntero = 0

            elif ascii == 10:

                cadena = cadena[1:]
                puntero = 0
                f += 1
                c = 1

            else:

                cadena = cadena[1:]
                puntero = 0
                c = 1

        for lexema in tokens:
            print(lexema)

    def find_Str(self, texto):
        f = self.f
        c = self.c
        tokens = self.tokens
        lexema = ''
        clave = ''

        for caracter in texto:

            ascii = ord(caracter)
            clave += caracter

            if ascii == 34:

                return lexema, texto[len(clave):]

            else:

                lexema += caracter

        return None, None

    def find_Number(self, texto):

        numero = ''
        clave = ''
        verificar = False

        for caracter in texto:

            clave += caracter
            ascii = ord(caracter)

            if ascii == 46:
                verificar = True

            if ascii == 34 or ascii == 32 or ascii == 10 or ascii == 9 or ascii == 44:

                if verificar:

                    return float(numero), texto[len(clave) - 1:]

                else:

                    return int(numero), texto[len(clave) - 1:]

            else:

                numero += caracter

        return None, None

    def operar(self):
        operacion = ""
        n1 = ''
        n2 = ''

        while self.tokens:

            lexema = self.tokens.pop(0)

            if lexema.operar(None) == "operacion":

                operacion = self.tokens.pop(0)

            elif lexema.operar(None) == "valor1":

                n1 = self.tokens.pop(0)

                if n1.operar(None) == "[":

                    n1 = self.operar()

            elif lexema.operar(None) == "valor2":

                n2 = self.tokens.pop(0)

                if n2.operar(None) == "[":

                    n2 = self.operar()

            if operacion and n1 and n2:

                return Aritmetica(n1, n2, operacion, f"Inicio: {operacion.get_F()}: {operacion.get_C()}",
                                  f"Fin: {n2.get_F()}: {n2.get_C()}")

            elif operacion and n1 and operacion.operar(None) == ('seno' or 'coseno' or 'tangente'):

                return Trigonometrica(n1, operacion, f"Inicio: {operacion.get_F()}: {operacion.get_C()}",
                                      f"Fin: {n2.get_F()}: {n2.get_C()}")

        return None

    def re_operar(self):

        while True:

            operacion = self.operar()

            if operacion:

                self.accion.append(operacion)

            else:

                break

        for instrucciones in self.accion:

            print(instrucciones.operar(None))

