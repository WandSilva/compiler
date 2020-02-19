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
        self.typeLexema = ""
        self.typeNRO = ""
        self.errorLineToken = 0
        self.listTokens = listTokens
        self.listErrors = []
        self.FirstGlobalValues = []
        self.FirstType = []
        self.FirstFunctions_Procedures = []
        self.FirstConstValuesDeclaration = []
        self.FirstConstValuesAttribution = []
        self.FirstConstMoreAttributions = []
        self.FirstVarValuesDeclaration = []
        self.FirstVarMoreAttributions = []
        self.FirstVarValuesAttribution = []
        self.FirstArrayVerification = []
        self.FirstIDE_Struct = []
        self.FirstIDE_Struct2 = []
        self.FirstFunctions_Procedures = []
        self.FirstValueConst = []
        self.FirstNumber = []
        self.FirstBooleanos = []
        
        self.FirstGlobalValues.append("const")
        self.FirstGlobalValues.append("var")
        self.FirstType.append("int")
        self.FirstType.append("real")
        self.FirstType.append("boolean")
        self.FirstType.append("string")
        self.FirstConstValuesDeclaration.extend(self.FirstType)
        self.FirstConstMoreAttributions.append(",")
        self.FirstConstValuesAttribution.append("IDE")
        self.FirstBooleanos.append("true")
        self.FirstBooleanos.append("false")
        self.FirstValueConst.append("NRO")
        self.FirstValueConst.append("CDC")
        self.FirstValueConst.extend(self.FirstBooleanos)
        self.FirstVarValuesDeclaration.extend(self.FirstType)
        self.FirstVarValuesDeclaration.append("typedef")
        self.FirstVarValuesDeclaration.append("struct")
        self.FirstVarMoreAttributions.append(",")
        self.FirstVarValuesAttribution.append("IDE")
        self.FirstArrayVerification.append("[")
        self.FirstIDE_Struct.append("IDE")
        self.FirstIDE_Struct2.append("{")
        self.FirstIDE_Struct2.append("extends")
        self.FirstFunctions_Procedures.append("function")
        self.FirstFunctions_Procedures.append("procedure")
    
    
    def starSyntaticAnalyzer(self):
        self.getNextToken()
        self.start()
       
        
    def getNextToken(self):
        token = self.listTokens[self.currentToken]
        self.lexemToken = token.lexema
        self.errorLineToken = token.linha
        self.typeLexema = token.tipo
        self.typeNRO = token.tipoNRO
    
        self.previousToken = self.currentToken
        self.currentToken = self.currentToken + 1
    
    def lookNextToken(self):
        token = self.listTokens[self.currentToken + 1]
        return token

    def lookNextNextToken(self):
        token = self.listTokens[self.currentToken + 2]
        return token

    def start(self):
        self.callGlobalValues()
        self.callFunctionProcedure()
    
    
    def callGlobalValues(self):
        if self.lexemToken in self.FirstGlobalValues:
            if self.lexemToken == "const":
                self.getNextToken()
                
                if self.lexemToken == "{":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
                
                self.callConstValuesDeclaration()
                
                if self.lexemToken == "}":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
                
                if self.lexemToken == "var":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "var"))
                
                if self.lexemToken == "{":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
                
                self.callVarValeusDeclaration()
                
                if self.lexemToken == "}":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
                    
            elif self.lexemToken == "var":
                self.getNextToken()
                
                if self.lexemToken == "{":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
                
                self.callVarValeusDeclaration()
                
                if self.lexemToken == "}":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
                
                if self.lexemToken == "const":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "const"))
                
                if self.lexemToken == "{":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
                
                self.callConstValuesDeclaration()
                
                if self.lexemToken == "}":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
                
    
    def callConstValuesDeclaration(self):
        if self.lexemToken in self.FirstConstValuesDeclaration:
            self.getNextToken()
            self.callConstValuesAttribution()
            self.callConstMoreAttributions()
            
            if self.lexemToken == ";":
                self.getNextToken()
            else:
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ";"))
                
            self.callConstValuesDeclaration()
    
        
    def callConstValuesAttribution(self):
        if self.typeLexema in self.FirstConstValuesAttribution:
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
        
        if self.lexemToken == "=":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "="))
            
        if self.lexemToken in self.FirstValueConst:
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "valor", ""))
    
    
    def callConstMoreAttributions(self):
        if self.lexemToken in self.FirstVarMoreAttributions:
            self.getNextToken()
            self.callConstValuesAttribution
            self.callConstMoreAttributions
    
        
    def callVarValeusDeclaration(self):
        if self.lexemToken in self.FirstVarValuesDeclaration:
            if self.lexemToken in self.FirstType:
                self.getNextToken()
                self.callVarValuesAttribution()
                self.callVarMoreAttributions()
                if self.lexemToken == ";":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ";"))
                    
                self.callVarValeusDeclaration()
                
            elif self.lexemToken == "typedef":
                self.getNextToken()
                if self.lexemToken == "struct":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "struct"))
                
                self.callIDE_Struct()
                self.callVarValuesDeclaration()
                
            elif self.lexemToken == "struct":
                self.getNextToken()
                self.callIDE_Struct()
                self.callVarValuesDeclaration()
        else:
            token = self.lookNextToken()
            token2 = self.lookNextNextToken()
            if token.tipo == "IDE" and token2.lexema in self.FirstIDE_Struct2:
                self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "struct"))
                self.callIDE_Struct()
                self.callVarValuesDeclaration()

            else:
                

            
    def callVarValuesAttribution(self):
        if self.typeLexema in self.FirstVarValuesAttribution:
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
        
        self.callArrayVarification()
        
            
    def callArrayVarification(self): 
        if self.lexemToken in self.FirstArrayVerification:
            self.getNextToken()
            if self.typeNRO == "NRO_I":
                self.getNextToken()
            else:
                self.listErrors.append(self.errorMessage(self.errorLineToken, "numeroI", ""))
                
            if self.lexemToken == "]":
                self.getNextToken()
            else:
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "]"))
            
            self.callArrayVarification
    
    
    def callVarMoreAttributions(self):
        if self.lexemToken in self.FirstVarMoreAttributions:
            self.getNextToken()
            self.callVarValuesAttribution()
            self.callVarMoreAttributions()
        

    def callIDE_Struct(self):
        if self.typeLexema in self.FirstIDE_Struct:
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
        
        self.callIDE_Struct2()
        
        
    def callIDE_Struct2(self):
        if self.lexemToken in self.FirstIDE_Struct2:
            if self.lexemToken == "{":
                self.callIDE_Struct2Aux()

            elif self.lexemToken == "extends":
                self.getNextToken()

                if self.typeLexema == "IDE":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))

                self.callIDE_Struct2Aux()
        
        else:
            token = self.lookNextToken()

            if token.tipo == "IDE":
                self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "extends"))
                self.getNextToken
                self.callIDE_Struct2Aux()
            else:
                self.callIDE_Struct2Aux()

    
    def callIDE_Struct2Aux(self):
        if self.lexemToken == "{":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))

        if self.lexemToken == "var":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "var"))

        if self.lexemToken == "{":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))

        self.callVarValeusDeclaration()

        if self.lexemToken == "}":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))

        if self.lexemToken == "}":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))

            
    def callFunctionProcedure(self):
        if self.lexemToken in self.FirstFunctions_Procedures:
            if self.lexemToken == "function":
                self.getNextToken()
                self.callFunction()

            elif self.lexemToken == "procedure":
                self.getNextToken()
                self.callProcedure()

        else:
            token = self.lookNextToken()
            if token.lexema in self.FirstType:
                self.callFunction()
            else:
                self.callProcedure()

    def callFunction(self):
        if self.lexemToken in self.FirstType:
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "tipo", ""))

        if self.typeLexema == "IDE":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))

        if self.lexemToken == "(":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "("))

        self.callParamList()

        if self.lexemToken == ")":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ")"))
        
        if self.lexemToken == "{":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))

        self.callVarFunctionsProcedures()
        self.callCommands()
        self.callReturn()

        if self.lexemToken == "}":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))

        self.callFunctionProcedure()

    def callProcedure(self):
        if self.typeLexema == "IDE":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))

        if self.lexemToken == "(":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "("))

        self.callParamList()

        if self.lexemToken == ")":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ")"))
        
        if self.lexemToken == "{":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))

        self.callVarFunctionsProcedures()
        self.callCommands()
        self.callReturn()

        if self.lexemToken == "}":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))

        self.callFunctionProcedure()


    def callParamList(self):


    def callVarFunctionsProcedures(self):
        if self.lexemToken

    
    def callCommands(self):

    
    def callReturn(self):

        
    def errorMessage(self, lineError, typeError, expectedValue):