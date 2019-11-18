#   EXA869 - MI - Processadores de Linguagem de Programação (2019.2)
#   Discentes: Aloisio Junior e Wanderson Silva

#   CLASSE TOKEN

class Token:

    def __init__(self):
        pass

    def __init__(self, lexema, linha, tipo, typeError):
        self.lexema = lexema
        self.linha = linha
        self.tipo = tipo
        self.hasError = False
        self.typeError = typeError
        
    def to_dict(self):
        token_dict = {"linha":str(self.linha+1),
                      "tipo":self.tipo,
                      "lexema":self.lexema,                      
                      "typeError":self.typeError}
        return token_dict