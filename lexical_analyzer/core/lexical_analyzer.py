from lexical_analyzer.token.token import Token
from lexical_analyzer.util.clean_code import CleanCode
import sys
import os.path
import string
import re


class LexicalAnalyzer:
    #auxLines = []
    tableSimbols = []
    #tokenNumber = 0
    #numErrors = 0

    def __init__(self, auxLines):
        self.auxLines = auxLines
        self.tokenNumber = 0
        self.tableSimbols = []
        self.numErrors = 0

    def increase_token_number(self):
        self.tokenNumber = self.tokenNumber + 1

    def start_lexical_analyzer(self):
        pass

    def classify_token_k(self):
        pass

    #@property
    def identify_token(self):
        lexeme = ""
        auxLine = ""
        errorLexeme = ""
        lineCDC = 0
        CDC = 0
        numLines = 0
        token = None
        sizeLexemes = len(self.auxLines)
        while numLines <= sizeLexemes - 1:
            auxLine = self.auxLines[numLines]
            sizeChars = len(self.auxLines[numLines])
            numChars = 0
            auxClass = ""
            lookAheadClass = ""
            auxLexeme = ""
            auxLookAheadLexeme = ""
            while numChars <= sizeChars - 1:
                if auxLexeme == "":
                    if auxLine[numChars] == " ":
                        numChars = numChars + 1
                        continue
                auxLexeme = auxLexeme + auxLine[numChars]
                auxClass = self.classify_token(auxLexeme)
                if auxClass == "INVALID_CLASS" and auxLexeme != " ":
                    errorLexeme = self.return_error_msg(auxClass)
                    token = Token(auxLexeme, numLines, auxClass, errorLexeme)
                    if errorLexeme is not None:
                        self.numErrors = self.numErrors + 1
                        token.hasError = True
                    self.tableSimbols.append(token)
                    auxLexeme = ""
                    auxLookAheadLexeme = ""
                    numChars = numChars + 1
                    token = None
                elif numChars + 1 <= sizeChars - 1:
                    numChars2 = numChars + 1
                    auxLookAheadLexeme = auxLexeme + auxLine[numChars2]
                    lookAheadClass = self.classify_token(auxLookAheadLexeme)
                    if auxClass == lookAheadClass:
                        numChars = numChars + 1
                    else:
                        if auxClass != "INVALID_CLASS" and lookAheadClass == "INVALID_CLASS":
                            errorLexeme = self.return_error_msg(auxClass)
                            token = Token(auxLexeme, numLines, auxClass, errorLexeme)
                            if errorLexeme is not None:
                                self.numErrors = self.numErrors + 1
                                token.hasError = True
                            self.tableSimbols.append(token)
                            auxLexeme = ""
                            auxLookAheadLexeme = ""
                            numChars = numChars + 1
                            token = None
                            continue
                        numChars = numChars + 1
                        
                else:
                    if auxLexeme != " ":
                        errorLexeme = self.return_error_msg(auxClass)
                        token = Token(auxLexeme, numLines, auxClass, errorLexeme)
                        if errorLexeme is not None:
                            self.numErrors = self.numErrors + 1
                            token.hasError = True
                        self.tableSimbols.append(token)
                        auxLexeme = ""
                        auxLookAheadLexeme = ""
                        numChars = numChars + 1
                        token = None
                        
            numLines = numLines + 1
        
        if token is not None:
            errorLexeme = self.return_error_msg(auxClass)
            token = Token(auxLexeme, numLines, auxClass, errorLexeme)
            if errorLexeme is not None:
                self.numErrors = self.numErrors + 1
                token.hasError = True
            self.tableSimbols.append(token)
            auxLexeme = ""
            auxLookAheadLexeme = ""
            token = None
            
        return self.tableSimbols

    def classify_token(self, lexeme):
        #   Verifica se é um identificador
        returnRegex = re.search("^([a-zA-Z]+\\w*)$", lexeme)
        if returnRegex:
            aux = self.is_reserved(lexeme)
            if aux:
                return "PRE"  # É uma palavra reservada
            else:
                return "IDE"  # É um identificador comum
        #   Verifica se é um identificador mal formado
        returnRegex = re.search("^([a-zA-Z]+\\w*)$", lexeme)
        if returnRegex:
            return "IDE_BF"
        #   Verifica se é um número completo
        returnRegex = re.search("^((-)?(\\s)*(\\d)+(\\.(\\d)+)?)$", lexeme)
        if returnRegex:
            return "NRO"
        #   Verifica se é um número incompleto
        returnRegex = re.search("^((-)?(\\d)+\\.?)$", lexeme)
        if returnRegex:
            return "NRO_INCOMPLETO"
        #   Verifica se é um operador relacional
        returnRegex = re.search("^((<=)|<|(==)|=|(>=)|>|(!=))$", lexeme)
        if returnRegex:
            return "REL"
        #   Verifica se é um operador aritimético
        returnRegex = re.search("^(((--)|-|(\\+\\+)|\\+|\\*|/))$", lexeme)
        if returnRegex:
            return "ART"
        #   Verifica se é um operador lógico
        returnRegex = re.search("^(!|(&&)|(\\|\\|))$", lexeme)
        if returnRegex:
            return "LOG"
        #   Verifica se é um operador lógico mal formado
        returnRegex = re.search("^(&|\\|)$", lexeme)
        if returnRegex:
            return "LOG_BF"
        #   Verifica se é um delimitador
        returnRegex = re.search("^(:|;|,|\\(|\\)|[|]|\\{|}|\\.)$", lexeme)
        if returnRegex:
            return "DEL"
        #   Verifica se é uma cadeia de caracteres
        returnRegex = re.search("^(\"((\\\\\")|[^\"]|\\n)*\")$", lexeme)
        if returnRegex:
            return "CDC"
        #   Verifica se é uma cadeia de caracteres mal formada
        returnRegex = re.search("^(\"((\\\\\")|[^\"]|\\n)*)$", lexeme)
        if returnRegex:
            return "CMF"
        #   Verifica se é uma caractere inválido
        returnRegex = re.search("^([^\\n\\w.()|+\\-<>=!/\\\\*\\[\\]{}\"\'\\\\\"]+)$", lexeme)
        if returnRegex:
            return "INVALID_CARACTER"
        #   Verifica se é um comentario mal formado
        #   Implementar aqui

        return "INVALID_CLASS"

    def separate_token(self):
        pass

    @staticmethod
    def is_reserved(lexeme):
        reserved = "var const typedef struct extends procedure function start return if else then while read print " \
                   "int real boolean string true false global local".split()
        if lexeme in reserved:
            return True
        else:
            return False

    @staticmethod
    def return_error_msg(classLexeme):
        errorMsg = ""
        if classLexeme == "IDE_BF":
            errorMsg = "Identificador mal formado"
            return errorMsg
        elif classLexeme == "NRO_INCOMPLETO":
            errorMsg = "Número mal formado"
            return errorMsg
        elif classLexeme == "LOG_BF":
            errorMsg = "Operador lógico mal formado"
            return errorMsg
        elif classLexeme == "CMF":
            errorMsg = "Cadeia de caracteres mal formada"
            return errorMsg
        elif classLexeme == "INVALID_CARACTER":
            errorMsg = "Caractere(s) inválido(s)"
            return errorMsg
        elif classLexeme == "CoMF":
            errorMsg = "Comentário mal formado"
            return errorMsg
        elif classLexeme == "INVALID_CLASS":
            errorMsg = "Caractere não reconhecido"
            return errorMsg
        return None

    def identify_comments(code):
        cc = CleanCode()
        newLine = ""  
        cleanSourceCode = []
        is_block_comment = False
        error_line = 0
        for index, line in enumerate(code):
            is_block_comment, newLine = cc.remove_comments(is_block_comment, line)
            cleanSourceCode.append(newLine)
            if(is_block_comment):
                error_line = index+1
            elif:
                error_line=0
            
        if is_block_comment:
            print("comentário mal formado, linha:"+str(line_number))