#   EXA869 - MI - Processadores de Linguagem de Programação (2019.2)
#   Discentes: Aloisio Junior e Wanderson Silva

#   CLASSE TOKEN
import re

class Token:

    def __init__(self):
        pass

    def __init__(self, lexema, linha, tipo, typeError):
        self.lexema = lexema
        self.linha = linha
        self.tipo = tipo
        self.hasError = False
        self.typeError = typeError
        self.tipoNRO = None
        
        if self.tipo == "NRO":
            returnRegex = re.search("^(\\d)+$", self.lexema)
            if returnRegex:
                self.tipoNRO = "NRO_I"
                
            returnRegex = re.search("^((-)?(\\d)+(\\.(\\d)+))$", self.lexema)
            if returnRegex:
                self.tipoNRO = "NRO_R"
        
    def to_dict(self):
        token_dict = {"linha":str(self.linha+1),
                      "tipo":self.tipo,
                      "tipoNRO":self.tipoNRO,
                      "lexema":self.lexema,                      
                      "typeError":self.typeError}
        return token_dict