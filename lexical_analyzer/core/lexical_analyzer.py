
import sys
import os.path
import string
import re

class LexicalAnalyzer:
    def __init__(self):
        tokenNumber = 0

    def increaseTokenNumber(self):
        self.tokenNumber = self.tokenNumber + 1

    def startLexicalAnalyzer(self):
        pass

    def identifyToken(self):
        pass

    def classifyToken (self, lexeme):
        #   Verifica se é um idenficador
        returnRegex = re.search("[a-zA-Z]+\\w*", lexeme)
        if returnRegex:
            aux = self.isReserved(lexeme)
            if aux:
                return "PRE"
            else:
                return "IDE"
        #   Verifica se é um número completo
        returnRegex = re.search("-?\\d+(\\.(\\d+))?", lexeme)
        if returnRegex:
            return "NRO"
        #   Verifica se é um número incompleto
        returnRegex = re.search("-?\\d+\\.?", lexeme)
        if returnRegex:
            return "NRO_INCOMPLETO"
        #   Verifica se é um operador relacional
        returnRegex = re.search("(<=)|<|(==)|=|(>=)|>|(!=)", lexeme)
        if returnRegex:
            return "REL"
        #   Verifica se é um operador aritimético
        returnRegex = re.search("(--)|-|(\\+\\+)|\\+|\\*|/", lexeme)
        if returnRegex:
            return "ART"
        #   Verifica se é um operador lógico
        returnRegex = re.search("!|(&&)|(\\|\\|)", lexeme)
        if returnRegex:
            return "LOG"
        #   Verifica se é um delimitador
        returnRegex = re.search(":|;|,|\\(|\\)|[|]|\\{|}|\\.", lexeme)
        if returnRegex:
            return "DEL"
        #   Verifica se é uma cadeia de caracteres
        returnRegex = re.search("\"((\\\\\")|[^\"]|\\n)*\"", lexeme)
        if returnRegex:
            return "CDC"
        #   Verifica se é uma cadeia de caracteres
        returnRegex = re.search("\"((\\\\\")|[^\"]|\\n)*", lexeme)
        if returnRegex:
            return "CMF"
        #   Verifica se é uma caractere inválido
        returnRegex = re.search("[^\\n\\w.()|+\\-<>=!/\\\\*\\[\\]{}\"\'\\\\\"]+", lexeme)
        if returnRegex:
            return "CARACTER_INVALID"
        #   Verifica se é um comentario mal formado
        #   Implementar aqui


    def separateToken(self):
        pass

    @staticmethod
    def isReserved(lexeme):
        reserved = "var const typedef struct extends procedure function start return if else then while read print " \
                   "int real boolean string true false global local".split()
        if lexeme in reserved:
            return True
        else:
            return False


'''
def main():
    i1 = "a=1;"
    i2 = "x>1"
    i3 = "x>=1"
    i4 = "x<1"
    i5 = "x<=1"
    i6 = "x!=1"
    i7 = "x = = 1"
    
    input_test = i7 
    print("entrada:" + input_test)  
    output = relational_operators(input_test)
    print(output)

def relational_operators (inputA):
    input_split = list(inputA)
    
    for i in range (0, len(input_split)):
        if(input_split[i] == "="):
            if(input_split[i+1] == '='):
                return "opetator: == "
            else:            
                return"operator: ="
        elif(input_split[i] == ">"):
            if(input_split[i+1] == '='):
                return "opetator: >="
            else:            
                return "operator: >"
        elif(input_split[i] == "<"):
            if(input_split[i+1] == '='):
                return "opetator: <="
            else:            
                return "operator: <"
        elif(input_split[i] == "!"):
            if(input_split[i+1] == '='):
                return "opetator: !="


if __name__ == "__main__":
    main()
'''