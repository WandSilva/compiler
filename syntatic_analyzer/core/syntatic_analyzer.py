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
        self.FirstConstValuesDeclaration = []
        self.FirstConstValuesAttribution = []
        self.FirstConstMoreAttributions = []
        self.FirstVarValuesDeclaration = []
        self.FirstVarMoreAttributions = []
        self.FirstVarValuesAttribution = []
        self.FirstArrayVerification = []
        self.FirstIDE_Struct = []
        self.FirstIDE_Struct2 = []
        self.FirstIDE_Struct2Aux = []
        self.FirstFunctions_Procedures = []
        self.FirstFunction = []
        self.FirstProcedure = []
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
        self.FirstCommands = []
        self.FirstReturn = []
        self.FirstParamList = []
        self.FirstMoreParamList = []
        self.FirstVarFunctionsProcedures = []
        self.FirstExpression = []

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
        self.FollowParamList = []
        self.FollowMoreParamList = []
        
        
        # Set os first's dos não terminais
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
        self.FirstIDE_Struct2Aux.append("{")
        self.FirstFunctions_Procedures.append("function")
        self.FirstFunctions_Procedures.append("procedure")
        self.FirstFunction.extend(self.FirstType)
        self.FirstProcedure.append("IDE")
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
        self.FirstParamList.extend(self.FirstType)
        self.FirstMoreParamList.append(",")
        self.FirstCommands.extend(self.FirstCommand)
        self.FirstVarFunctionsProcedures.append("var")
        self.FirstExpression

        # Set os follow's dos não terminais
        self.FollowGlobalValeus.extend(self.FirstFunctions_Procedures)
        self.FollowConstValuesDeclaration.append("}")
        self.FollowConstValuesDeclaration.extend(self.FirstConstValuesDeclaration)
        self.FollowVarValuesDeclaration.append("}")
        self.FollowVarValuesDeclaration.extend(self.FirstVarValuesDeclaration)
        self.FollowConstValuesAttribution.extend(self.FirstConstMoreAttributions)
        self.FollowConstMoreAttributions.append(";")
        self.FollowVarValuesAttribution.extend(self.FirstVarMoreAttributions)
        self.FollowVarMoreAttributions.append(";")
        self.FollowVarMoreAttributions.extend(self.FirstVarMoreAttributions)
        self.FollowIDE_Struct.extend(self.FirstVarValuesDeclaration)
        self.FollowIDE_Struct2.extend(self.FollowIDE_Struct)
        self.FollowIDE_Struct2Aux.extend(self.FollowIDE_Struct2)
        self.FollowArrayVerification.extend(self.FollowVarValuesAttribution)
        self.FollowFunctionProcedure.append("Ç") # Adicionar o simbolo no final de lexico e elterar os tratamentos pra final de codigo no sintatico
        self.FollowFunction.extend(self.FirstFunctions_Procedures)
        self.FollowProcedure.extend(self.FirstFunctions_Procedures)
        self.FollowCommand.extend(self.FirstCommands)
        self.FollowCommands.extend(self.FirstCommands)
        self.FollowVarFunctionsProcedures.extend(self.FirstCommands)
        self.FollowReturn.append("}")
        self.FollowParamList.append(")")
        self.FollowMoreParamList.extend(self.FollowParamList)
    

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
        if self.lexemToken in self.FirstGlobalValues:
            if self.lexemToken == "const":
                self.getNextToken()
                
                if self.lexemToken == "{":
                    self.getNextToken()
                else:
                    while (not ((self.lexemToken == "{") or (self.lexemToken in self.FirstConstValuesDeclaration) or (self.lexemToken in self.FollowGlobalValeus)) and (not self.lexemToken == None)):
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
                    while (not ((self.lexemToken == "{") or (self.lexemToken in self.FirstVarValuesDeclaration) or (self.lexemToken in self.FollowGlobalValeus)) and (not self.lexemToken == None)):
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
                    while (not ((self.lexemToken == "{") or (self.lexemToken in self.FirstVarValuesDeclaration) or (self.lexemToken in self.FollowGlobalValeus)) and (not self.lexemToken == None)):
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
                    while (not ((self.lexemToken == "{") or (self.lexemToken in self.FirstConstValuesDeclaration) or (self.lexemToken in self.FollowGlobalValeus)) and (not self.lexemToken == None)):
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
            while (not (self.lexemToken in self.FirstGlobalValues or self.lexemToken in self.FollowGlobalValeus) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FollowGlobalValeus))
                self.getNextToken()
            if self.lexemToken in self.FirstGlobalValues:
                self.callGlobalValues()
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
                while (not ((self.lexemToken == ";") or (self.lexemToken in self.FollowConstValuesDeclaration)) and (not self.lexemToken == None)):
                    self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, [";"]))
                    self.getNextToken()
                if (not self.lexemToken == ";"):
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ";"))
                elif (self.lexemToken == ";"):
                    self.getNextToken()

            self.callConstValuesDeclaration()

        else:
            while (not ((self.lexemToken in self.FirstConstValuesDeclaration) or (self.lexemToken in self.FollowConstValuesDeclaration)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FollowConstValuesDeclaration))
                self.getNextToken()

            if self.lexemToken in self.FirstConstValuesDeclaration:
                self.callConstValuesDeclaration()
            else:
                pass
 
        
    def callConstValuesAttribution(self):
        if self.typeLexema in self.FirstConstValuesAttribution:
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
            while (not ((self.lexemToken == "=") or (self.lexemToken in self.FirstValueConst or self.typeLexema in self.FirstValueConst) or (self.lexemToken in self.FollowConstValuesAttribution)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["="]))
                self.getNextToken()
            if (not self.lexemToken == "="):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "="))
            elif (self.lexemToken == "="):
                self.getNextToken()
            
        if (self.lexemToken in self.FirstValueConst or self.typeLexema in self.FirstValueConst):
            self.getNextToken()
        else:
            while(not((self.lexemToken in self.FirstValueConst or self.typeLexema in self.FirstValueConst) or (self.lexemToken in self.FollowConstValuesAttribution)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FirstValueConst))
                self.getNextToken()
            if (not (self.lexemToken in self.FirstValueConst or self.typeLexema in self.FirstValueConst)):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "valor", ""))
            elif (self.lexemToken in self.FirstValueConst or self.typeLexema in self.FirstValueConst):
                self.getNextToken()  
    
    
    def callConstMoreAttributions(self):
        if self.lexemToken in self.FirstVarMoreAttributions:
            self.getNextToken()
            self.callConstValuesAttribution
            self.callConstMoreAttributions

        else:
            while(not((self.lexemToken in self.FirstConstMoreAttributions) or (self.lexemToken in self.FollowConstMoreAttributions)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FollowConstMoreAttributions))
                self.getNextToken()
            if self.lexemToken in self.FirstConstMoreAttributions:
                self.callConstMoreAttributions()
        

    def callVarValuesDeclaration(self):
        if self.lexemToken in self.FirstVarValuesDeclaration:
            if self.lexemToken in self.FirstType:
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
                    while (not ((self.lexemToken == "struct") or (self.lexemToken in self.FirstIDE_Struct) or (self.lexemToken in self.FollowVarValuesDeclaration)) and (not self.lexemToken == None)):
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
            #if token.tipo == "IDE" and token2.lexema in self.FirstIDE_Struct2:
            #    self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "struct"))
            #    self.callIDE_Struct()
            #    self.callVarValuesDeclaration()
            while (not (self.lexemToken in self.FirstVarValuesDeclaration or self.lexemToken in self.FollowVarValuesDeclaration) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FollowVarValuesDeclaration))
                self.getNextToken()
            if self.lexemToken in self.FirstVarValuesDeclaration:
                self.callVarValuesDeclaration()
            else:
                pass

            
    def callVarValuesAttribution(self):
        if self.typeLexema in self.FirstVarValuesAttribution:
            self.getNextToken()
        else:
            while (not ((self.typeLexema == "IDE") or (self.lexemToken in self.FirstArrayVerification) or (self.lexemToken in self.FollowVarValuesAttribution)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["IDE"]))
                self.getNextToken()
            if (not self.typeLexema == "IDE"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
            elif (self.typeLexema == "IDE"):
                self.getNextToken()
        
        self.callArrayVarification()
        
            
    def callArrayVarification(self): 
        if self.lexemToken in self.FirstArrayVerification:
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
                while (not ((self.lexemToken == "]") or (self.lexemToken in self.FirstArrayVerification) or (self.lexemToken in self.FollowArrayVerification)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["]"]))
                        self.getNextToken()
                if (not self.typeNRO == "]"):
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "]"))
                elif (self.lexemToken == "]"):
                    self.getNextToken()
            
            self.callArrayVarification()

        else:
            while(not((self.lexemToken in self.FirstArrayVerification) or (self.lexemToken in self.FollowArrayVerification)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FirstArrayVerification))
                self.getNextToken()
            if self.lexemToken in self.FirstArrayVerification:
                self.callArrayVarification()
            else:
                pass
    
    
    def callVarMoreAttributions(self):
        if self.lexemToken in self.FirstVarMoreAttributions:
            self.getNextToken()
            self.callVarValuesAttribution()
            self.callVarMoreAttributions()
        else:
            while(not((self.lexemToken in self.FirstVarMoreAttributions) or (self.lexemToken in self.FollowVarMoreAttributions)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FollowVarMoreAttributions))
                self.getNextToken()

        

    def callIDE_Struct(self):
        if self.typeLexema in self.FirstIDE_Struct:
            self.getNextToken()
        else:
            while(not((self.typeLexema in self.FirstIDE_Struct) or (self.lexemToken in self.FirstIDE_Struct2 or self.typeLexema in self.FirstIDE_Struct2) or (self.lexemToken in self.FollowIDE_Struct)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FirstIDE_Struct))
                self.getNextToken()
            if (not (self.typeLexema == "IDE")):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
            elif (self.typeLexema == "IDE"):
                self.getNextToken()
        
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
                    while(not((self.typeLexema == "IDE") or (self.lexemToken in self.FirstIDE_Struct2Aux) or (self.lexemToken in self.FollowIDE_Struct)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["IDE"]))
                        self.getNextToken()
                    if (not (self.typeLexema == "IDE")):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
                    elif (self.typeLexema == "IDE"):
                        self.getNextToken()

                self.callIDE_Struct2Aux()
        
        else:
            while(not((self.lexemToken in self.FirstIDE_Struct2) or (self.lexemToken in self.FollowIDE_Struct2)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FirstIDE_Struct2))
                self.getNextToken()
            if self.lexemToken in self.FirstIDE_Struct2:
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
            while (not ((self.lexemToken == "{") or (self.lexemToken in self.FirstVarValuesDeclaration) or (self.lexemToken in self.FollowIDE_Struct2Aux)) and (not self.lexemToken == None)):
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
        if self.lexemToken in self.FirstFunctions_Procedures:
            if self.lexemToken == "function":
                self.getNextToken()
                self.callFunction()

            elif self.lexemToken == "procedure":
                self.getNextToken()
                self.callProcedure()

        else:
            while (not (self.lexemToken in self.FirstFunctions_Procedures) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FirstFunctions_Procedures))
                self.getNextToken()
            
            if self.lexemToken in self.FirstFunctions_Procedures:
                self.callFunctionProcedure()
            else:
                pass

    def callFunction(self):
        if self.lexemToken in self.FirstType:
            self.getNextToken()
        else:
            while (not ((self.lexemToken in self.FirstType) or (self.typeLexema == "IDE") or (self.lexemToken in self.FollowFunction)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FirstType))
                self.getNextToken()
            if (not self.lexemToken in self.FirstType):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "tipo", ""))
            elif (self.lexemToken in self.FirstType):
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
            while (not ((self.lexemToken == "(") or (self.lexemToken in self.FirstParamList) or (self.lexemToken in self.FollowFunction)) and (not self.lexemToken == None)):
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
            while (not ((self.lexemToken == "{") or (self.lexemToken in self.FirstVarFunctionsProcedures) or (self.lexemToken in self.FollowFunction)) and (not self.lexemToken == None)):
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
            while (not ((self.lexemToken == "}") or (self.lexemToken in self.FirstFunctions_Procedures) or (self.lexemToken in self.FollowFunction)) and (not self.lexemToken == None)):
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
            while (not ((self.lexemToken == "(") or (self.lexemToken in self.FirstParamList) or (self.lexemToken in self.FollowProcedure)) and (not self.lexemToken == None)):
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
            while (not ((self.lexemToken == "{") or (self.lexemToken in self.FirstVarFunctionsProcedures) or (self.lexemToken in self.FollowProcedure)) and (not self.lexemToken == None)):
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
            while (not ((self.lexemToken == "}") or (self.lexemToken in self.FirstFunctions_Procedures) or (self.lexemToken in self.FollowProcedure)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["}"]))
                self.getNextToken()
            if (not self.lexemToken == "}"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
            elif (self.lexemToken == "}"):
                self.getNextToken()

        self.callFunctionProcedure()


    def callParamList(self):
        if self.lexemToken in self.FirstType:
            if self.lexemToken in self.FirstType:
                self.getNextToken()
            else:
                while (not ((self.lexemToken in self.FirstType) or (self.typeLexema == "IDE") or (self.lexemToken in self.FollowParamList)) and (not self.lexemToken == None)):
                    self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FirstType))
                    self.getNextToken()
                if (not self.lexemToken in self.FirstType):
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "tipo", ""))
                elif (self.lexemToken in self.FirstType)):
                    self.getNextToken()
            
            if self.typeLexema == "IDE":
                self.getNextToken()
            else:
                while (not ((self.typeLexema == "IDE") or (self.lexemToken in self.FirstMoreParam) or (self.lexemToken in self.FollowParamList)) and (not self.lexemToken == None)):
                    self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FirstType))
                    self.getNextToken()
                if (not self.typeLexema == "IDE"):
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
                elif (self.typeLexema == "IDE")):
                    self.getNextToken()

            self.callMoreParam()

        else:
            while (not ((self.lexemToken in self.FirstType) or (self.lexemToken in self.FollowParamList)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FirstType))
                self.getNextToken()
            if (self.lexemToken in self.FirstType):
                self.callParamList()
            else:
                pass


    def callMoreParam(self):
        if self.lexemToken == ",":
            self.getNextToken()
            
            self.callParamList()
        else:
            while (not ((self.lexemToken == ",") or (self.lexemToken in self.FollowMoreParamList)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, [","]))
                self.getNextToken()
            if self.lexemToken == ",":
                self.callMoreParam()
            else:
                pass

    
    def callParamListInFuncProc(self):

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
            while (not ((self.lexemToken == "{") or (self.lexemToken in self.FirstVarValuesDeclaration) or (self.lexemToken in self.FollowVarFunctionsProcedures)) and (not self.lexemToken == None)):
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
        if self.lexemToken in self.FirstCommand or self.typeLexema in self.FirstCommand:
            self.callCommand()
            self.callCommands()

        else:
            while (not ((self.lexemToken in self.FirstCommand) or (self.typeLexema in self.FirstCommand) or (self.lexemToken in self.FollowCommand)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FirstCommand))
                self.getNextToken()
            if self.lexemToken in self.FirstCommand or self.typeLexema in self.FirstCommand:
                self.callCommands()


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
        # Quando for chamar os parametros, chamar por: callParamListInFuncProc
        pass

    
    def callExpression(self):
        pass


    def callFullLogicalExp(self):
        pass

    def callFullRelationalEx(self):
        pass

    
    def callOptLogExp(self):
        pass

    def callPossRelExp(self):
        pass

    def callLogicalExp(self):
        pass

    def callRelationalExp(self):
        pass

    def callEqualExp(self):
        pass

    def callInequalExp(self):
        pass


    def callAritmeticExp(self):
        pass


    def callOperation(self):
        pass


    def callOpSum(self):
        pass

    def OpMultiplication(self):
        pass


    def callOpUnary(self):
        pass


    def callUnaryOp(self):
        pass


    def callSubExp(self):
        if self.lexemToken in self.FirstCallVariable:
            self.callCallVariable()
        elif self.typeLexema in self.FirstNumber ou :
            self.getNextToken()
        elif self.typeLexema in self.FirstBooleanos:
            self.getNextToken()
        else:
            pass



    def callCallVariable(self):
        pass
    

    def callModifier(self):
        pass
    
    def callReturn(self):
        if self.lexemToken in self.FirstReturn:
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "return") or (self.lexemToken in self.FirstExpression) or (self.lexemToken in self.FollowReturn)) and (not self.lexemToken == None)):
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
