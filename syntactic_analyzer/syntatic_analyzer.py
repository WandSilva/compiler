#   EXA869 - MI - Processadores de Linguagem de Programação (2019.2)
#   Discentes: Aloisio Junior e Wanderson Silva

#   ANALISADOR SINTÁTICO

import re


class SyntaticAnalyzer:
    
    def __init__(self, listTokens):
        self.currentToken = 0
        self.previousToken = 0
        self.numberFile = 0
        self.lexemToken = ""
        self.errorLineToken = 0
        self.listTokens = listTokens
        self.FirstGlobalValues = []
        self.FirstType = []
        self.FirstFunctions_Procedures = []
        self.FirstConstValuesDeclaration = []
        self.FirstConstValuesAttribution = []
        self.FirstConstMoreAttributions = []
        self.FirstVarValuesDeclaration = []
        self.FirstFunctions_Procedures = []
        self.FirstValueConst = []
        self.FirstNumber = []
        self.FirstBooleanos = []
        self
        
        FirstGlobalValues.append("const")
        FirstGlobalValues.append("var")
        FirstType.append("int")
        FirstType.append("real")
        FirstType.append("boolean")
        FirstType.append("string")
        FirstConstValuesDeclaration.append(FirstType)
        FirstConstMoreAttributions.append(",")
        FirstConstValuesAttribution.append("IDE")
        FirstBooleanos.append("true")
        FirstBooleanos.append("false")
        FirstValueConst.append(FirstNumber)
        FirstValueConst.append("CDC")
        FirstValueConst.append(FirstBooleanos)
        
    
    def starSyntaticAnalyzer(self):
        self.getNextToken()
        
        
    def getNextToken(self):
        token = self.listTokens[self.currentToken]
        self.lexemToken = token.lexema
        self.errorLineToken = token.linha
        self.previousToken = self.currentToken
        self.currentToken = self.currentToken + 1
        