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
        self.FirstModifier = []
        self.FirstCommandIf = []
        self.FirstCallVariable = []
        self.FirstCommandWhile = []
        self.FirstCommandRead = []
        self.FirstCommandPrint = []
        self.FirstUnaryOP = []
        self.FirstAssignment = []
        self.FirstCallProcedure_Function = []
        self.FirstCommand = []
        self.FirstReturn = []
        
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
        self.FirstModifier.append("local")
        self.FirstModifier.append("global")
        self.FirstCommandIf.append("if")
        self.FirstCallVariable.extend(self.FirstModifier)
        self.FirstCallVariable.append("IDE")
        self.FirstCommandWhile.append("while")
        self.FirstCommandRead.append("read")
        self.FirstCommandPrint.append("print")
        self.FirstUnaryOP
        self.FirstAssignment.extend(self.FirstCallVariable)
        self.FirstAssignment.extend(self.FirstUnaryOP)
        self.FirstCallProcedure_Function.append("IDE")
        self.FirstCommand.extend(self.FirstCommandIf)
        self.FirstCommand.extend(self.FirstCommandWhile)
        self.FirstCommand.extend(self.FirstCommandRead)
        self.FirstCommand.extend(self.FirstCommandPrint)
        self.FirstCommand.extend(self.FirstAssignment)
        self.FirstCommand.extend(self.FirstCallProcedure_Function)
        self.FirstReturn.append("return")
    
    
    def starSyntaticAnalyzer(self):
        self.getNextToken()
        self.start()
       
        
    def getNextToken(self):
        token = self.listTokens[self.currentToken]
        if token is not None:
            self.lexemToken = token.lexema
            self.errorLineToken = token.linha
            self.typeLexema = token.tipo
            self.typeNRO = token.tipoNRO
            self.previousToken = self.currentToken
            self.currentToken = self.currentToken + 1

        else:
            self.lexemToken = None

        
    
    def lookNextToken(self):
        token = self.listTokens[self.currentToken + 1]
        return token

    def lookNextNextToken(self):
        token = self.listTokens[self.currentToken + 2]
        return token

    def start(self):
        controlPanic = False
        
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
                    while (not (self.lexemToken in self.FirstConstValuesDeclaration) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FirstConstValuesDeclaration))
                        self.getNextToken()
                
                self.callConstValuesDeclaration()
                
                if self.lexemToken == "}":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
                    while (not (self.lexemToken == "var") and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["var"]))
                        self.getNextToken()
                
                if self.lexemToken == "var":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "var")) #*
                    while (not (self.lexemToken == "{") and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken))
                        self.getNextToken()
                
                if self.lexemToken == "{":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
                    while (not (self.lexemToken in self.FirstVarValuesDeclaration) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken))
                        self.getNextToken()
                
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
                    while (not (self.lexemToken in self.FirstVarValuesDeclaration) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken))
                        self.getNextToken()
                
                self.callVarValeusDeclaration()
                
                if self.lexemToken == "}":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
                    while (not (self.lexemToken == "const") and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken))
                        self.getNextToken()
                
                if self.lexemToken == "const":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "const"))
                    while (not (self.lexemToken == "{") and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken))
                        self.getNextToken()
                
                if self.lexemToken == "{":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
                    while (not (self.lexemToken in self.FirstConstValuesDeclaration) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken))
                        self.getNextToken()
                
                self.callConstValuesDeclaration()
                
                if self.lexemToken == "}":
                    self.getNextToken()
                else:
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
        
        else:
            pass
                
    
    def callConstValuesDeclaration(self):
        if self.lexemToken in self.FirstConstValuesDeclaration:
            self.getNextToken()
            self.callConstValuesAttribution()
            self.callConstMoreAttributions()
            
            if self.lexemToken == ";":
                self.getNextToken()
            else:
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ";"))
                while (not (self.lexemToken in self.FirstConstValuesDeclaration) and (not self.lexemToken == None)):
                    self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken))
                    self.getNextToken()
                
            self.callConstValuesDeclaration()

        else:
            #if self.typeLexema == "IDE":
            #    self.listErrors.append(self.errorMessage(self.errorLineToken, "tipo", ""))
            #else:
            while (not (self.lexemToken in self.FirstConstValuesDeclaration or self.lexemToken == "}" ) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken))
                self.getNextToken()

            if self.lexemToken is not None and (not self.lexemToken == "}"):
                self.callConstValuesDeclaration()
 
        
    def callConstValuesAttribution(self):
        if self.typeLexema in self.FirstConstValuesAttribution:
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
            while (not (self.lexemToken == "=") and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken))
                self.getNextToken()
        
        if self.lexemToken == "=":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "="))
            while (not (self.lexemToken in self.FirstValueConst or self.typeLexema in self.FirstValueConst) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken))
                self.getNextToken()
            
        if (self.lexemToken in self.FirstValueConst or self.typeLexema in self.FirstValueConst):
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "valor", ""))
    
    
    def callConstMoreAttributions(self):
        if self.lexemToken in self.FirstVarMoreAttributions:
            self.getNextToken()
            self.callConstValuesAttribution
            self.callConstMoreAttributions

        else:
            pass
    
        
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
                pass
                

            
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
            while (not (self.lexemToken in self.FirstFunctions_Procedures) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FirstCallProcedure_Function))
                self.getNextToken()
            
            if self.lexemToken is not None:
                self.callFunctionProcedure()

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
        if self.lexemToken in self.FirstType or self.typeLexema == "IDE":
            if self.lexemToken in self.FirstType:
                self.getNextToken()
            else:
                self.listErrors.append(self.errorMessage(self.errorLineToken, "tipo", ""))
            
            if self.typeLexema == "IDE":
                self.getNextToken()
            else:
                self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))

            self.callMoreParam()

        else:
            pass


    def callMoreParam(self):
        if self.lexemToken == ",":
            self.getNextToken()
            self.callParamList()
        else:
            pass


    def callVarFunctionsProcedures(self):
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

    
    def callCommands(self):
        if self.lexemToken in self.FirstCommand or self.typeLexema in self.FirstCommand:
            self.callCommand()
            self.callCommands()

        else:
            pass


    def callCommand(self):
        if self.lexemToken in self.FirstCommandIf:
            self.callIfStatement()

        elif self.lexemToken in self.FirstCommandWhile:
            self.callWhileStatement()

        elif self.lexemToken in self.FirstCommandRead:
            self.callReadStatement()

        elif self.lexemToken in self.FirstCommandPrint:
            self.calPrintStatement()

        elif self.lexemToken in self.FirstAssignment or self.typeLexema in self.FirstAssignment:
            self.callAssignment()

        elif self.typeLexema in self.FirstCallProcedure_Function:
            self.callProcedureFunction()

    
    def callIfStatement(self):
        if self.lexemToken in self.FirstCommandIf:
            self.getNextToken()
        else: 
            self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", "if"))
            self.getNextToken()
        if self.lexemToken == '(':
            self.getNextToken()
            self.callFullLogicalExp()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "("))
            self.getNextToken()
        if self.lexemToken == ')':
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ")"))
            self.getNextToken()
        if self.lexemToken == 'then':
            self.getNextToken()
        else: 
            self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", "then"))
            self.getNextToken()
        if self.lexemToken == '{':
            self.getNextToken
            self.callComands()
        else: 
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
            self.getNextToken()
        if self.lexemToken == '}':
            self.getNextToken
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
            self.getNextToken()

    
    def callWhileStatement(self):
        if self.lexemToken in self.FirstCommandWhile:
            self.getNextToken()
        else: 
            self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", "while"))
            self.getNextToken()
        if self.lexemToken == '(':
            self.getNextToken()
            self.callFullLogicalExp()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "("))
            self.getNextToken()
        if self.lexemToken == ')':
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ")"))
            self.getNextToken()
        if self.lexemToken == '{':
            self.getNextToken
            self.callComands()
        else: 
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
            self.getNextToken()
        if self.lexemToken == '}':
            self.getNextToken
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
            self.getNextToken()

    
    def callReadStatement(self):
        pass


    def calPrintStatement(self):
        pass


    def callAssignment(self):
        pass


    def callProcedureFunction(self):
        pass

    
    def callExpression(self):
        pass


    def callFullLogicalExp(self):
        pass

    
    def callReturn(self):
        if self.lexemToken in self.FirstReturn:
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "return"))
        
        self.callExpression()

        if self.lexemToken == ";":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ";"))

        
    def errorMessage(self, lineError, typeError, expectedValue):
        pass

    
    def errorMessagePanic(self, lineError, typeLexem, valeuLexem, expectativeCon):
        