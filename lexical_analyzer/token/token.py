
class Token:

    def __init__(self):
        pass


    def __init__(self, lexema, linha, tipo, typeError):
        self.lexema = lexema
        self.linha = linha
        self.tipo = tipo
        self.hasError = False
        self.typeError = typeError