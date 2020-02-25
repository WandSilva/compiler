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
        self.firstGlobalValues = []
        self.firstType = []
        self.firstConstValuesDeclaration = []
        self.firstConstValuesAttribution = []
        self.firstConstMoreAttributions = []
        self.firstVarValuesDeclaration = []
        self.firstVarMoreAttributions = []
        self.firstVarValuesAttribution = []
        self.firstArrayVerification = []
        self.firstIDE_Struct = []
        self.firstIDE_Struct2 = []
        self.firstIDE_Struct2Aux = []
        self.firstFunctions_Procedures = []
        self.firstFunction = []
        self.firstProcedure = []
        self.firstValueConst = []
        self.firstNumber = []  #a lista ta vazia
        self.firstBooleanos = []
        self.firstModifier = []
        self.firstCommandIf = []
        self.firstCallVariable = []
        self.firstCommandWhile = []
        self.firstCommandRead = []
        self.firstCommandPrint = []
        self.firstUnaryOP = []
        self.firstOpUnary = []
        self.firstAssignment = []
        self.firstCallProcedure_Function = []
        self.firstCommand = []
        self.firstCommands = []
        self.firstReturn = []
        self.firstParamList = []
        self.firstVarFunctionsProcedures = []
        self.firstExpression = []
        self.firstFinalValue = []
        self.firstTimesDivision = []
        self.firstPlusMinus = []
        self.firstAritmeticExp = []
        self.firstRelationalMorePrec = []
        self.firstRelationalLessPrec = []
        self.firstOptRelExp = []
        self.firstLogicalOperators = []
        self.firstLogicalExp = []

        self.FollowGlobalValeus = []
        self.FollowConstValuesDeclaration = []
        self.FollowVarValuesDeclaration = []
        self.FollowConstValuesAttribution = []
        self.FollowConstMoreAttributions = []
        self.FollowVarValuesAttribution = []
        self.FollowVarMoreAttributions = []
        self.FollowIDE_Struct = []
        self.FollowIDE_Struct2 = []
        self.FollowIDE_Struct2Aux = []
        self.FollowArrayVerification = []
        self.FollowFunctionProcedure = []
        self.FollowFunction = []
        self.FollowProcedure = []
        self.FollowCommand = []
        self.FollowCommands = []
        self.FollowReturn = []
        self.FollowVarFunctionsProcedures = []
        
        
        # Set os first's dos não terminais
        self.firstGlobalValues.append("const")
        self.firstGlobalValues.append("var")
        self.firstType.append("int")
        self.firstType.append("real")
        self.firstType.append("boolean")
        self.firstType.append("string")
        self.firstConstValuesDeclaration.extend(self.firstType)
        self.firstConstMoreAttributions.append(",")
        self.firstConstValuesAttribution.append("IDE")
        self.firstBooleanos.append("true")
        self.firstBooleanos.append("false")
        self.firstValueConst.append("NRO")
        self.firstValueConst.append("CDC")
        self.firstValueConst.extend(self.firstBooleanos)
        self.firstVarValuesDeclaration.extend(self.firstType)
        self.firstVarValuesDeclaration.append("typedef")
        self.firstVarValuesDeclaration.append("struct")
        self.firstVarMoreAttributions.append(",")
        self.firstVarValuesAttribution.append("IDE")
        self.firstArrayVerification.append("[")
        self.firstIDE_Struct.append("IDE")
        self.firstIDE_Struct2.append("{")
        self.firstIDE_Struct2.append("extends")
        self.firstIDE_Struct2Aux.append("{")
        self.firstFunctions_Procedures.append("function")
        self.firstFunctions_Procedures.append("procedure")
        self.firstFunction.extend(self.firstType)
        self.firstProcedure.append("IDE")
        self.firstModifier.append("local")
        self.firstModifier.append("global")
        self.firstCommandIf.append("if")
        self.firstCallVariable.extend(self.firstModifier)
        self.firstCallVariable.append("IDE") #ainda tem esse IDE?
        self.firstCommandWhile.append("while")
        self.firstCommandRead.append("read")
        self.firstCommandPrint.append("print")
        self.firstUnaryOP.append('++')
        self.firstUnaryOP.append('--')
        self.firstAssignment.extend(self.firstCallVariable)
        self.firstAssignment.extend(self.firstUnaryOP)
        self.firstCallProcedure_Function.append("IDE")
        self.firstCommand.extend(self.firstCommandIf)
        self.firstCommand.extend(self.firstCommandWhile)
        self.firstCommand.extend(self.firstCommandRead)
        self.firstCommand.extend(self.firstCommandPrint)
        self.firstCommand.extend(self.firstAssignment)
        self.firstCommand.extend(self.firstCallProcedure_Function)
        self.firstReturn.append("return")
        self.firstParamList
        self.firstCommands.extend(self.firstCommand)
        self.firstVarFunctionsProcedures.append("var")
        self.firstExpression
        self.firstFinalValue.extend(self.firstCallVariable)
        self.firstFinalValue.extend(self.firstBooleanos)
        self.firstFinalValue.extend(self.firstNumber)
        self.firstTimesDivision.append('*')
        self.firstTimesDivision.append('/')
        self.firstOpUnary.extend(self.firstUnaryOP)
        self.firstOpUnary.extend(self.firstFinalValue)
        self.firstOpUnary.append('(')
        self.firstPlusMinus.append('+')
        self.firstPlusMinus.append('-')
        self.firstAritmeticExp.extend(self.firstOpUnary)
        self.firstAritmeticExp.append('(')
        self.firstRelationalMorePrec.append('>')
        self.firstRelationalMorePrec.append('<')
        self.firstRelationalMorePrec.append('>=')
        self.firstRelationalMorePrec.append('<=')
        self.firstRelationalLessPrec.append('==')
        self.firstRelationalLessPrec.append('!=')
        self.firstOptRelExp.extend(self.firstRelationalLessPrec)
        self.firstOptRelExp.extend(self.firstRelationalMorePrec)
        self.firstOptRelExp.extend(self.firs    tAritmeticExp)
        self.firstLogicalOperators.append('&&')
        self.firstLogicalOperators.append('||')
        self.firstLogicalExp.extend(self.firstAritmeticExp)
        self.firstLogicalExp.extend('(')


        # Set os follow's dos não terminais
        self.FollowGlobalValeus.extend(self.firstFunctions_Procedures)
        self.FollowConstValuesDeclaration.append("}")
        self.FollowConstValuesDeclaration.extend(self.firstConstValuesDeclaration)
        self.FollowVarValuesDeclaration.append("}")
        self.FollowVarValuesDeclaration.extend(self.firstVarValuesDeclaration)
        self.FollowConstValuesAttribution.extend(self.firstConstMoreAttributions)
        self.FollowConstMoreAttributions.append(";")
        self.FollowVarValuesAttribution.extend(self.firstVarMoreAttributions)
        self.FollowVarMoreAttributions.append(";")
        self.FollowVarMoreAttributions.extend(self.firstVarMoreAttributions)
        self.FollowIDE_Struct.extend(self.firstVarValuesDeclaration)
        self.FollowIDE_Struct2.extend(self.FollowIDE_Struct)
        self.FollowIDE_Struct2Aux.extend(self.FollowIDE_Struct2)
        self.FollowArrayVerification.extend(self.FollowVarValuesAttribution)
        self.FollowFunctionProcedure.append("Ç") # Adicionar o simbolo no final de lexico e elterar os tratamentos pra final de codigo no sintatico
        self.FollowFunction.extend(self.firstFunctions_Procedures)
        self.FollowProcedure.extend(self.firstFunctions_Procedures)
        self.FollowCommand.extend(self.firstCommands)
        self.FollowCommands.extend(self.firstCommands)
        self.FollowVarFunctionsProcedures.extend(self.firstCommands)
        self.FollowReturn.append("}")
    

    def letsWork(self):
        self.starSyntaticAnalyzer()
        self.writeFiles()
        self.cleanStructs()


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
        self.callGlobalValues()
        self.callFunctionProcedure()
    
    
    def callGlobalValues(self):
        if self.lexemToken in self.firstGlobalValues:
            if self.lexemToken == "const":
                self.getNextToken()
                
                if self.lexemToken == "{":
                    self.getNextToken()
                else:
                    while (not ((self.lexemToken == "{") or (self.lexemToken in self.firstConstValuesDeclaration) or (self.lexemToken in self.FollowGlobalValeus)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["{"]))
                        self.getNextToken()
                    if (not self.lexemToken == "{"):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
                    elif (self.lexemToken == "{"):
                        self.getNextToken()
                
                self.callConstValuesDeclaration()
                
                if self.lexemToken == "}":
                    self.getNextToken()
                else:
                    while (not ((self.lexemToken == "}") or (self.lexemToken == "var") or (self.lexemToken in self.FollowGlobalValeus)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["}"]))
                        self.getNextToken()
                    if (not self.lexemToken == "}"):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
                    elif (self.lexemToken == "}"):
                        self.getNextToken()
                
                if self.lexemToken == "var":
                    self.getNextToken()
                else:
                    while (not ((self.lexemToken == "var") or (self.lexemToken == "{") or (self.lexemToken in self.FollowGlobalValeus)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["var"]))
                        self.getNextToken()
                    if (not self.lexemToken == "var"):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "var"))
                    elif (self.lexemToken == "var"):
                        self.getNextToken()
                
                if self.lexemToken == "{":
                    self.getNextToken()
                else:
                    while (not ((self.lexemToken == "{") or (self.lexemToken in self.firstVarValuesDeclaration) or (self.lexemToken in self.FollowGlobalValeus)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["{"]))
                        self.getNextToken()
                    if (not self.lexemToken == "{"):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
                    elif (self.lexemToken == "{"):
                        self.getNextToken()
                    
                self.callVarValuesDeclaration()
                
                if self.lexemToken == "}":
                    self.getNextToken()
                else:
                    while (not ((self.lexemToken == "}") or (self.lexemToken in self.FollowGlobalValeus)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["}"]))
                        self.getNextToken()
                    if (not self.lexemToken == "}"):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
                    elif (self.lexemToken == "}"):
                        self.getNextToken()
                    
            elif self.lexemToken == "var":
                self.getNextToken()
                
                if self.lexemToken == "{":
                    self.getNextToken()
                else:
                    while (not ((self.lexemToken == "{") or (self.lexemToken in self.firstVarValuesDeclaration) or (self.lexemToken in self.FollowGlobalValeus)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["{"]))
                        self.getNextToken()
                    if (not self.lexemToken == "{"):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
                    elif (self.lexemToken == "{"):
                        self.getNextToken()
                
                self.callVarValuesDeclaration()
                
                if self.lexemToken == "}":
                    self.getNextToken()
                else:
                    while (not ((self.lexemToken == "}") or (self.lexemToken == "const") or (self.lexemToken in self.FollowGlobalValeus)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["}"]))
                        self.getNextToken()
                    if (not self.lexemToken == "}"):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
                    elif (self.lexemToken == "}"):
                        self.getNextToken()
                
                if self.lexemToken == "const":
                    self.getNextToken()
                else:
                    while (not ((self.lexemToken == "const") or (self.lexemToken == "{") or (self.lexemToken in self.FollowGlobalValeus)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["const"]))
                        self.getNextToken()
                    if (not self.lexemToken == "const"):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "const"))
                    elif (self.lexemToken == "const"):
                        self.getNextToken()
                
                if self.lexemToken == "{":
                    self.getNextToken()
                else:
                    while (not ((self.lexemToken == "{") or (self.lexemToken in self.firstConstValuesDeclaration) or (self.lexemToken in self.FollowGlobalValeus)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["{"]))
                        self.getNextToken()
                    if (not self.lexemToken == "{"):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
                    elif (self.lexemToken == "{"):
                        self.getNextToken()
                
                self.callConstValuesDeclaration()
                
                if self.lexemToken == "}":
                    self.getNextToken()
                else:
                    while (not ((self.lexemToken == "}") or (self.lexemToken in self.FollowGlobalValeus)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["}"]))
                        self.getNextToken()
                    if (not self.lexemToken == "}"):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
                    elif (self.lexemToken == "}"):
                        self.getNextToken()
        
        else:
            while (not (self.lexemToken in self.firstGlobalValues or self.lexemToken in self.FollowGlobalValeus) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FollowGlobalValeus))
                self.getNextToken()
            if self.lexemToken in self.firstGlobalValues:
                self.callGlobalValues()
            else:
                pass
                
    
    def callConstValuesDeclaration(self):
        if self.lexemToken in self.firstConstValuesDeclaration:
            self.getNextToken()
            
            self.callConstValuesAttribution()
            self.callConstMoreAttributions()
            
            if self.lexemToken == ";":
                self.getNextToken()
            else:                
                while (not ((self.lexemToken == ";") or (self.lexemToken in self.FollowConstValuesDeclaration)) and (not self.lexemToken == None)):
                    self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, [";"]))
                    self.getNextToken()
                if (not self.lexemToken == ";"):
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ";"))
                elif (self.lexemToken == ";"):
                    self.getNextToken()

            self.callConstValuesDeclaration()

        else:
            while (not ((self.lexemToken in self.firstConstValuesDeclaration) or (self.lexemToken in self.FollowConstValuesDeclaration)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FollowConstValuesDeclaration))
                self.getNextToken()

            if self.lexemToken in self.firstConstValuesDeclaration:
                self.callConstValuesDeclaration()
            else:
                pass
 
        
    def callConstValuesAttribution(self):
        if self.typeLexema in self.firstConstValuesAttribution:
            self.getNextToken()
        else:
            while (not ((self.typeLexema == "IDE") or (self.lexemToken == "=") or (self.lexemToken in self.FollowConstValuesAttribution)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["IDE"]))
                self.getNextToken()
            if (not self.typeLexema == "IDE"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
            elif (self.typeLexema == "IDE"):
                self.getNextToken()
        
        if self.lexemToken == "=":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "=") or (self.lexemToken in self.firstValueConst or self.typeLexema in self.firstValueConst) or (self.lexemToken in self.FollowConstValuesAttribution)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["="]))
                self.getNextToken()
            if (not self.lexemToken == "="):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "="))
            elif (self.lexemToken == "="):
                self.getNextToken()
            
        if (self.lexemToken in self.firstValueConst or self.typeLexema in self.firstValueConst):
            self.getNextToken()
        else:
            while(not((self.lexemToken in self.firstValueConst or self.typeLexema in self.firstValueConst) or (self.lexemToken in self.FollowConstValuesAttribution)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstValueConst))
                self.getNextToken()
            if (not (self.lexemToken in self.firstValueConst or self.typeLexema in self.firstValueConst)):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "valor", ""))
            elif (self.lexemToken in self.firstValueConst or self.typeLexema in self.firstValueConst):
                self.getNextToken()  
    
    
    def callConstMoreAttributions(self):
        if self.lexemToken in self.firstVarMoreAttributions:
            self.getNextToken()
            self.callConstValuesAttribution
            self.callConstMoreAttributions

        else:
            while(not((self.lexemToken in self.firstConstMoreAttributions) or (self.lexemToken in self.FollowConstMoreAttributions)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FollowConstMoreAttributions))
                self.getNextToken()
            if self.lexemToken in self.firstConstMoreAttributions:
                self.callConstMoreAttributions()
        

    def callVarValuesDeclaration(self):
        if self.lexemToken in self.firstVarValuesDeclaration:
            if self.lexemToken in self.firstType:
                self.getNextToken()
                self.callVarValuesAttribution()
                self.callVarMoreAttributions()
                if self.lexemToken == ";":
                    self.getNextToken()
                else:
                    while (not ((self.lexemToken == ";") or (self.lexemToken in self.FollowVarValuesDeclaration)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, [";"]))
                        self.getNextToken()
                    if (not self.lexemToken == ";"):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ";"))
                    elif (self.lexemToken == ";"):
                        self.getNextToken()
                    
                self.callVarValuesDeclaration()
                
            elif self.lexemToken == "typedef":
                self.getNextToken()
                if self.lexemToken == "struct":
                    self.getNextToken()
                else:
                    while (not ((self.lexemToken == "struct") or (self.lexemToken in self.firstIDE_Struct) or (self.lexemToken in self.FollowVarValuesDeclaration)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["struct"]))
                        self.getNextToken()
                    if (not self.lexemToken == "struct"):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "struct"))
                    elif (self.lexemToken == "struct"):
                        self.getNextToken()
                
                self.callIDE_Struct()
                self.callVarValuesDeclaration()
                
            elif self.lexemToken == "struct":
                self.getNextToken()
                self.callIDE_Struct()
                self.callVarValuesDeclaration()

        else:
            #token = self.lookNextToken()
            #token2 = self.lookNextNextToken()
            #if token.tipo == "IDE" and token2.lexema in self.firstIDE_Struct2:
            #    self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "struct"))
            #    self.callIDE_Struct()
            #    self.callVarValuesDeclaration()
            while (not (self.lexemToken in self.firstVarValuesDeclaration or self.lexemToken in self.FollowVarValuesDeclaration) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FollowVarValuesDeclaration))
                self.getNextToken()
            if self.lexemToken in self.firstVarValuesDeclaration:
                self.callVarValuesDeclaration()
            else:
                pass

            
    def callVarValuesAttribution(self):
        if self.typeLexema in self.firstVarValuesAttribution:
            self.getNextToken()
        else:
            while (not ((self.typeLexema == "IDE") or (self.lexemToken in self.firstArrayVerification) or (self.lexemToken in self.FollowVarValuesAttribution)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["IDE"]))
                self.getNextToken()
            if (not self.typeLexema == "IDE"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
            elif (self.typeLexema == "IDE"):
                self.getNextToken()
        
        self.callArrayVarification()
        
            
    def callArrayVarification(self): 
        if self.lexemToken in self.firstArrayVerification:
            self.getNextToken()
            if self.typeNRO == "NRO_I":
                self.getNextToken()
            else:
                while (not ((self.typeNRO == "NRO_I") or (self.lexemToken == "]") or (self.lexemToken in self.FollowArrayVerification)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["NRO_I"]))
                        self.getNextToken()
                if (not self.typeNRO == "NRO_I"):
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "NRO_I", ""))
                elif (self.typeNRO == "NRO_I"):
                    self.getNextToken()
                                
            if self.lexemToken == "]":
                self.getNextToken()
            else:
                while (not ((self.lexemToken == "]") or (self.lexemToken in self.firstArrayVerification) or (self.lexemToken in self.FollowArrayVerification)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["]"]))
                        self.getNextToken()
                if (not self.typeNRO == "]"):
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "]"))
                elif (self.lexemToken == "]"):
                    self.getNextToken()
            
            self.callArrayVarification()

        else:
            while(not((self.lexemToken in self.firstArrayVerification) or (self.lexemToken in self.FollowArrayVerification)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstArrayVerification))
                self.getNextToken()
            if self.lexemToken in self.firstArrayVerification:
                self.callArrayVarification()
            else:
                pass
    
    
    def callVarMoreAttributions(self):
        if self.lexemToken in self.firstVarMoreAttributions:
            self.getNextToken()
            self.callVarValuesAttribution()
            self.callVarMoreAttributions()
        else:
            while(not((self.lexemToken in self.firstVarMoreAttributions) or (self.lexemToken in self.FollowVarMoreAttributions)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FollowVarMoreAttributions))
                self.getNextToken()

        

    def callIDE_Struct(self):
        if self.typeLexema in self.firstIDE_Struct:
            self.getNextToken()
        else:
            while(not((self.typeLexema in self.firstIDE_Struct) or (self.lexemToken in self.firstIDE_Struct2 or self.typeLexema in self.firstIDE_Struct2) or (self.lexemToken in self.FollowIDE_Struct)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstIDE_Struct))
                self.getNextToken()
            if (not (self.typeLexema == "IDE")):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
            elif (self.typeLexema == "IDE"):
                self.getNextToken()
        
        self.callIDE_Struct2()
        
        
    def callIDE_Struct2(self):
        if self.lexemToken in self.firstIDE_Struct2:
            if self.lexemToken == "{":
                self.callIDE_Struct2Aux()

            elif self.lexemToken == "extends":
                self.getNextToken()

                if self.typeLexema == "IDE":
                    self.getNextToken()
                else:
                    while(not((self.typeLexema == "IDE") or (self.lexemToken in self.firstIDE_Struct2Aux) or (self.lexemToken in self.FollowIDE_Struct)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["IDE"]))
                        self.getNextToken()
                    if (not (self.typeLexema == "IDE")):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
                    elif (self.typeLexema == "IDE"):
                        self.getNextToken()

                self.callIDE_Struct2Aux()
        
        else:
            while(not((self.lexemToken in self.firstIDE_Struct2) or (self.lexemToken in self.FollowIDE_Struct2)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstIDE_Struct2))
                self.getNextToken()
            if self.lexemToken in self.firstIDE_Struct2:
                self.callIDE_Struct2()
            else:
                pass

    
    def callIDE_Struct2Aux(self):
        if self.lexemToken == "{":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "{") or (self.lexemToken == "var") or (self.lexemToken in self.FollowIDE_Struct2Aux)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["{"]))
                self.getNextToken()
            if (not self.lexemToken == "{"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
            elif (self.lexemToken == "{"):
                self.getNextToken()

        if self.lexemToken == "var":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "var") or (self.lexemToken == "{") or (self.lexemToken in self.FollowIDE_Struct2Aux)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["var"]))
                self.getNextToken()
            if (not self.lexemToken == "var"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "var"))
            elif (self.lexemToken == "var"):
                self.getNextToken()

        if self.lexemToken == "{":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "{") or (self.lexemToken in self.firstVarValuesDeclaration) or (self.lexemToken in self.FollowIDE_Struct2Aux)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["{"]))
                self.getNextToken()
            if (not self.lexemToken == "{"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
            elif (self.lexemToken == "{"):
                self.getNextToken()

        self.callVarValuesDeclaration()

        if self.lexemToken == "}":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "}") or (self.lexemToken == "}") or (self.lexemToken in self.FollowIDE_Struct2Aux)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["}"]))
                self.getNextToken()
            if (not self.lexemToken == "}"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
            elif (self.lexemToken == "}"):
                self.getNextToken()

        if self.lexemToken == "}":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "}") or (self.lexemToken in self.FollowIDE_Struct2Aux)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["}"]))
                self.getNextToken()
            if (not self.lexemToken == "}"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
            elif (self.lexemToken == "}"):
                self.getNextToken()

            
    def callFunctionProcedure(self):
        if self.lexemToken in self.firstFunctions_Procedures:
            if self.lexemToken == "function":
                self.getNextToken()
                self.callFunction()

            elif self.lexemToken == "procedure":
                self.getNextToken()
                self.callProcedure()

        else:
            while (not (self.lexemToken in self.firstFunctions_Procedures) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstFunctions_Procedures))
                self.getNextToken()
            
            if self.lexemToken in self.firstFunctions_Procedures:
                self.callFunctionProcedure()
            else:
                pass

    def callFunction(self):
        if self.lexemToken in self.firstType:
            self.getNextToken()
        else:
            while (not ((self.lexemToken in self.firstType) or (self.typeLexema == "IDE") or (self.lexemToken in self.FollowFunction)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstType))
                self.getNextToken()
            if (not self.lexemToken in self.firstType):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "tipo", ""))
            elif (self.lexemToken in self.firstType):
                self.getNextToken()

        if self.typeLexema == "IDE":
            self.getNextToken()
        else:
            while (not ((self.typeLexema == "IDE") or (self.lexemToken == "(") or (self.lexemToken in self.FollowFunction)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["IDE"]))
                self.getNextToken()
            if (not self.typeLexema == "IDE"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
            elif (self.typeLexema == "IDE"):
                self.getNextToken()

        if self.lexemToken == "(":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "(") or (self.lexemToken in self.firstParamList) or (self.lexemToken in self.FollowFunction)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["("]))
                self.getNextToken()
            if (not self.lexemToken == "("):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "("))
            elif (self.lexemToken == "("):
                self.getNextToken()

        self.callParamList()

        if self.lexemToken == ")":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == ")") or (self.lexemToken == "{") or (self.lexemToken in self.FollowFunction)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, [")"]))
                self.getNextToken()
            if (not self.lexemToken == ")"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ")"))
            elif (self.lexemToken == ")"):
                self.getNextToken()
        
        if self.lexemToken == "{":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "{") or (self.lexemToken in self.firstVarFunctionsProcedures) or (self.lexemToken in self.FollowFunction)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["{"]))
                self.getNextToken()
            if (not self.lexemToken == "{"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
            elif (self.lexemToken == "{"):
                self.getNextToken()

        self.callVarFunctionsProcedures()
        self.callCommands()
        self.callReturn()

        if self.lexemToken == "}":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "}") or (self.lexemToken in self.firstFunctions_Procedures) or (self.lexemToken in self.FollowFunction)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["}"]))
                self.getNextToken()
            if (not self.lexemToken == "}"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
            elif (self.lexemToken == "}"):
                self.getNextToken()
            

        self.callFunctionProcedure()


    def callProcedure(self):
        if self.typeLexema == "IDE":
            self.getNextToken()
        else:
            while (not ((self.typeLexema == "IDE") or (self.lexemToken == "(") or (self.lexemToken in self.FollowProcedure)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["IDE"]))
                self.getNextToken()
            if (not self.typeLexema == "IDE"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
            elif (self.typeLexema == "IDE"):
                self.getNextToken()

        if self.lexemToken == "(":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "(") or (self.lexemToken in self.firstParamList) or (self.lexemToken in self.FollowProcedure)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["("]))
                self.getNextToken()
            if (not self.lexemToken == "("):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "("))
            elif (self.lexemToken == "("):
                self.getNextToken()

        self.callParamList()

        if self.lexemToken == ")":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == ")") or (self.lexemToken == "{") or (self.lexemToken in self.FollowProcedure)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, [")"]))
                self.getNextToken()
            if (not self.lexemToken == ")"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ")"))
            elif (self.lexemToken == ")"):
                self.getNextToken()
        
        if self.lexemToken == "{":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "{") or (self.lexemToken in self.firstVarFunctionsProcedures) or (self.lexemToken in self.FollowProcedure)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["{"]))
                self.getNextToken()
            if (not self.lexemToken == "{"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
            elif (self.lexemToken == "{"):
                self.getNextToken()

        self.callVarFunctionsProcedures()
        self.callCommands()
        self.callReturn()

        if self.lexemToken == "}":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "}") or (self.lexemToken in self.firstFunctions_Procedures) or (self.lexemToken in self.FollowProcedure)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["}"]))
                self.getNextToken()
            if (not self.lexemToken == "}"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
            elif (self.lexemToken == "}"):
                self.getNextToken()

        self.callFunctionProcedure()


    def callParamList(self):
        if self.lexemToken in self.firstType or self.typeLexema == "IDE":
            if self.lexemToken in self.firstType:
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
            while (not ((self.lexemToken == "var") or (self.lexemToken == "{") or (self.lexemToken in self.FollowVarFunctionsProcedures)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["var"]))
                self.getNextToken()
            if (not self.lexemToken == "var"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "var"))
            elif (self.lexemToken == "var"):
                self.getNextToken()

        if self.lexemToken == "{":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "{") or (self.lexemToken in self.firstVarValuesDeclaration) or (self.lexemToken in self.FollowVarFunctionsProcedures)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["{"]))
                self.getNextToken()
            if (not self.lexemToken == "{"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
            elif (self.lexemToken == "{"):
                self.getNextToken()
        
        self.callVarValuesDeclaration()

        if self.lexemToken == "}":
            self.getNextToken()
        else: 
            while (not ((self.lexemToken == "}") or (self.lexemToken in self.FollowVarFunctionsProcedures)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["}"]))
                self.getNextToken()
            if (not self.lexemToken == "}"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
            elif (self.lexemToken == "}"):
                self.getNextToken()

    
    def callCommands(self):
        if self.lexemToken in self.firstCommand or self.typeLexema in self.firstCommand:
            self.callCommand()
            self.callCommands()

        else:
            while (not ((self.lexemToken in self.firstCommand) or (self.typeLexema in self.firstCommand) or (self.lexemToken in self.FollowCommand)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstCommand))
                self.getNextToken()
            if self.lexemToken in self.firstCommand or self.typeLexema in self.firstCommand:
                self.callCommands()


    def callCommand(self):
        if self.lexemToken in self.firstCommandIf:
            self.callIfStatement()

        elif self.lexemToken in self.firstCommandWhile:
            self.callWhileStatement()

        elif self.lexemToken in self.firstCommandRead:
            self.callReadStatement()

        elif self.lexemToken in self.firstCommandPrint:
            self.calPrintStatement()

        elif self.lexemToken in self.firstAssignment or self.typeLexema in self.firstAssignment:
            self.callAssignment()

        elif self.typeLexema in self.firstCallProcedure_Function:
            self.callProcedureFunction()            

    
    def callIfStatement(self):
        if self.lexemToken in self.firstCommandIf:
            self.getNextToken()
        else: 
            self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", "if"))
            self.getNextToken()
        if self.lexemToken == '(':
            self.getNextToken()
            self.callRelationalExp()
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
            self.callCommands()
        else: 
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
            self.getNextToken()
        if self.lexemToken == '}':
            self.getNextToken
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
            self.getNextToken()

    
    def callWhileStatement(self):
        if self.lexemToken in self.firstCommandWhile:
            self.getNextToken()
        else: 
            self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", "while"))
            self.getNextToken()
        if self.lexemToken == '(':
            self.getNextToken()
            self.callRelationalExp()
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
            self.callCommands()
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
        if self.lexemToken in self.firstAritmeticExp:
            self.callRelationalExp()
        else:
            pass
        if self.lexemToken in self.firstLogicalOperators:
                self.callOptLogicalExp()
        else:
            pass



    def callRelationalExp(self):
        if self.lexemToken in self.firstAritmeticExp:
            self.callAritmeticExp()
        else:
            pass
        if self.lexemToken in self.firstOptRelExp:
            self.callOptRelExp()
        else:
            pass


    def callOptLogicalExp(self):
        if self.lexemToken in self.firstLogicalOperators:
                self.getNextToken()
        else:
            pass
        if self.lexemToken in self.firstLogicalExp:
                self.callLogicalExp()
        else:
            pass
        

    #regra não fatorada
    def callLogicalExp(self):
        if self.lexemToken in self.firstAritmeticExp:
            self.callRelationalExp()
            if self.lexemToken in self.firstLogicalOperators:
                self.getNextToken()
            else:
                pass
            if self.lexemToken in self.firstLogicalExp:
                self.callLogicalExp()
        elif self.lexemToken == '(':
            self.getNextToken()
            if self.lexemToken in self.firstLogicalExp:
                self.callLogicalExp()
            else:
                pass
            if self.lexemToken == ')':
                self.getNextToken()
        


    def callOptRelExp(self):
        if self.lexemToken in self.firstAritmeticExp:
            self.callAritmeticExp()
            if self.lexemToken in self.firstRelationalMorePrec:
                self.callInequalityExp()
            if self.lexemToken in self.firstRelationalLessPrec:
                self.callEqualityExp()
            else:
                pass
        elif self.lexemToken in self.firstRelationalLessPrec:
            self.getNextToken()
            if self.lexemToken in self.firstAritmeticExp:
                self.callAritmeticExp()
            else:
                pass
        elif self.lexemToken in self.firstRelationalMorePrec:
            self.getNextToken()
            if self.lexemToken in self.firstAritmeticExp:
                self.callAritmeticExp()
            else:
                pass



    def callEqualityExp(self):
        if self.lexemToken in self.firstRelationalLessPrec:
            self.getNextToken()
        else:
            pass
        if self.lexemToken in self.firstAritmeticExp:
            self.callAritmeticExp()
        else:
            pass
        if self.lexemToken in self.firstRelationalMorePrec:
            self.callInequalityExp()
        else:
            pass
        if self.lexemToken in self.firstRelationalLessPrec:
            self.callEqualityExp()
        else:
            pass

    def callInequalityExp(self):
        if self.lexemToken in self.firstRelationalMorePrec:
            self.getNextToken()
        else:
            pass
        if self.lexemToken in self.firstAritmeticExp:
            self.callAritmeticExp()
        else:
            pass
        if self.lexemToken in self.firstRelationalMorePrec:
            self.callInequalityExp()
        else:
            pass


    def callAritmeticExp(self):
        if self.lexemToken in self.firstOpUnary:
            self.callOperation()
        else:
            pass
        if self.lexemToken in self.firstPlusMinus:
            self.getNextToken()
        elif self.lexemToken == '(':
            self.getNextToken()
            #incompleto
            


    def callOperation(self):
        if self.lexemToken in self.firstOpUnary:
            self.callOpUnary()
        else:
            pass
        if self.lexemToken in self.firstTimesDivision:
            self.callOpMultiplication()
        else: 
            pass


    def callOpSum(self):
        if self.lexemToken in self.firstPlusMinus:
            self.getNextToken()
        else:
            pass
        if self.lexemToken in self.firstOpUnary:
            self.callOperation()
        else:
            pass
        if self.lexemToken in self.firstPlusMinus:
            self.getNextToken()
        else:
            pass
        
        

    def callOpMultiplication(self):
        if self.lexemToken in self.firstTimesDivision:
            self.getNextToken()
        else:
            pass
        if self.lexemToken in self.firstUnaryOP:
            self.callOpUnary()
        else:
            pass
        if self.lexemToken in self.firstTimesDivision:
            self.callOpMultiplication()
        


    def callOpUnary(self):
        if self.lexemToken in self.firstUnaryOP:
            self.callUnaryOp()
        elif self.lexemToken in self.firstFinalValue:
            self.callFinalValue()
        elif self.lexemToken == '(':
            self.getNextToken()
            if self.lexemToken in self.firstAritmeticExp:
                self.callAritmeticExp()
            else:
                pass
            if self.lexemToken == ')':
                self.getNextToken()
        else:
            pass



    def callUnaryOp(self):
        if self.lexemToken in self.firstUnaryOP:
            self.getNextToken()
            if self.lexemToken in self.firstFinalValue:
                self.callFinalValue()
        elif self.lexemToken in self.firstFinalValue:
            self.callFinalValue()
            if self.lexemToken in self.firstUnaryOP:
                self.getNextToken()
        elif self.lexemToken == '!':
            if self.lexemToken in self.firstCallVariable:
                self.callCallVariable()



    def callFinalValue(self):
        if self.lexemToken in self.firstCallVariable:
            self.callCallVariable()
        elif self.typeLexema == 'NRO':
            self.getNextToken()
        elif self.getNextToken in self.firstBooleanos:
            self.getNextToken()
        else:
            pass

    def callCallVariable(self):
        if self.lexemToken in self.firstCallVariable:
            self.getNextToken()
        if self.lexemToken == '.':
            self.getNextToken()
        if self.typeLexema == 'IDE':
            self.getNextToken()
        if self.lexemToken in self.firstCallPath: #criar isso aqui
            self.callPath()
        else:
            pass

    
    
    def callReturn(self):
        if self.lexemToken in self.firstReturn:
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "return") or (self.lexemToken in self.firstExpression) or (self.lexemToken in self.FollowReturn)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["return"]))
                self.getNextToken()
            if (not self.lexemToken == "return"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "return"))
            elif (self.lexemToken == "return"):
                self.getNextToken()
        
        self.callExpression()

        if self.lexemToken == ";":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ";"))

        
    def errorMessage(self, lineError, typeError, expectedValue):
        pass

    
    def errorMessagePanic(self, lineError, typeLexem, valeuLexem, expectativeCon):
        pass


    def writeFiles(self):
        pass


    def cleanStructs(self):
        pass