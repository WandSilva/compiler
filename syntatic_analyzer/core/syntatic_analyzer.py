#   EXA869 - MI - Processadores de Linguagem de Programação (2019.2)
#   Discentes: Aloisio Junior e Wanderson Silva

#   ANALISADOR SINTÁTICO

import re
from semantic_analyzer.semantic import semantic_analyzer


class SyntaticAnalyzer:
    
    def __init__(self, listTokens):
        
        self.semantic = semantic_analyzer()

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
        self.firstNumber = []  
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
        self.firstMoreParam = []
        self.firstVarFunctionsProcedures = []
        self.firstExpression = [] #esta vazio
        self.firstFinalValue = []
        self.firstTimesDivision = []
        self.firstPlusMinus = []
        self.firstAritmeticExp = []
        self.firstRelationalMorePrec = []
        self.firstRelationalLessPrec = []
        self.firstPossRelExp = []
        self.firstLogicalOperators = []
        self.firstLogicalExp = []
        self.firstRelacionalExp = []
        self.firstReadParam = []
        self.firstMoreReadParams = []
        self.firstPrintParams = []
        self.firstPrintParam = []
        self.firstMorePrintParams = []
        self.firstAssign2 = []
        self.firstPaths = []
        self.firstStruct = []
        self.firstMatrAssign = []
        self.firstCell = []
        self.firstParamListInFuncProc = []
        self.firstMoreRealParam = []
        self.firstRealParam = []
        self.firstValueParam = []

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
        self.FollowCommandIf = []
        self.FollowCommandWhile = []
        self.FollowCommandRead = []
        self.FollowCommandPrint = []
        self.FollowAssignment = []
        self.FollowCallProcedureFunction = []
        self.FollowReadParam = []
        self.FollowMoreReadParams = []
        self.FollowPrintParams = []
        self.FollowPrintParam = []
        self.FollowMorePrintParams = []
        self.FollowAssign2 = []
        self.FollowPaths = []
        self.FollowStruct = []
        self.FollowMatrAssign = []
        self.FollowCell = []
        self.FollowCallVariable = []
        self.FollowUnary_Op = []
        self.FollowFinal_Value = []
        self.FollowParamListInFuncProc = []
        self.FollowRealParam = []
        self.FollowValueParam = []
        self.FollowMoreRealParam = []
        
        
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
        self.firstNumber.append("NRO")
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
        # self.firstCallVariable.append("IDE") #ainda tem esse IDE?
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
        self.firstParamList.extend(self.firstType)
        self.firstMoreParam.append(",")
        self.firstCommands.extend(self.firstCommand)
        self.firstVarFunctionsProcedures.append("var")
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
        self.firstPossRelExp.extend(self.firstRelationalLessPrec)
        self.firstPossRelExp.extend(self.firstRelationalMorePrec)
        self.firstLogicalOperators.append('&&')
        self.firstLogicalOperators.append('||')
        self.firstLogicalExp.extend(self.firstAritmeticExp)
        self.firstLogicalExp.append('(')
        self.firstRelacionalExp.append(self.firstAritmeticExp)
        self.firstRelacionalExp.append('(')
        self.firstReadParam.extend(self.firstCallVariable)
        self.firstMoreReadParams.append(",")
        self.firstPrintParam.append("CDC")
        self.firstPrintParam.extend(self.firstCallVariable)
        self.firstPrintParams.extend(self.firstPrintParam)
        self.firstMorePrintParams.append(",")
        self.firstExpression.extend(self.firstAritmeticExp)
        self.firstExpression.extend(self.firstLogicalExp)
        self.firstAssign2.append("CDC")
        self.firstAssign2.append("NRO") 
        self.firstAssign2.extend(self.firstCallProcedure_Function)
        self.firstAssign2.extend(self.firstExpression)
        self.firstValueParam.extend(self.firstNumber)
        self.firstValueParam.append("CDC")
        self.firstValueParam.extend(self.firstBooleanos)
        self.firstRealParam.extend(self.firstValueParam)
        self.firstRealParam.extend(self.firstCallVariable)
        self.firstMoreRealParam.append(",")
        self.firstParamListInFuncProc.extend(self.firstRealParam)
        self.firstStruct.append(".")
        self.firstCell.append("[")
        self.firstMatrAssign.extend(self.firstCell)
        self.firstPaths.extend(self.firstStruct)
        self.firstPaths.extend(self.firstMatrAssign)


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
        self.FollowFunction.extend(self.firstFunctions_Procedures)
        self.FollowProcedure.extend(self.firstFunctions_Procedures)
        self.FollowCommand.extend(self.firstCommands)
        self.FollowCommands.extend(self.firstCommands)
        self.FollowVarFunctionsProcedures.extend(self.firstCommands)
        self.FollowReturn.append("}")
        self.FollowParamList.append(")")
        self.FollowMoreParamList.extend(self.FollowParamList)
        self.FollowCommandIf.extend(self.FollowCommand)
        self.FollowCommandWhile.extend(self.FollowCommand)
        self.FollowCommandRead.extend(self.FollowCommand)
        self.FollowCommandPrint.extend(self.FollowCommand)
        self.FollowAssignment.extend(self.FollowCommand)
        self.FollowCallProcedureFunction.extend(self.FollowCommand)
        self.FollowReadParam.append(")")
        self.FollowMoreReadParams.extend(self.FollowReadParam)
        self.FollowPrintParams.append(")")
        self.FollowPrintParam.extend(self.firstMorePrintParams)
        self.FollowMorePrintParams.extend(self.FollowPrintParams)
        self.FollowUnary_Op
        self.FollowFinal_Value
        self.FollowRealParam 
        self.FollowCallVariable.extend(self.FollowUnary_Op)
        self.FollowCallVariable.extend(self.FollowFinal_Value)
        self.FollowCallVariable.extend(self.FollowMoreReadParams)
        self.FollowCallVariable.extend(self.FollowPrintParam)
        self.FollowCallVariable.extend(self.FollowRealParam)
        self.FollowCallVariable.append("=")
        self.FollowCallVariable.append("]")
        self.FollowParamListInFuncProc.append(")")
        self.FollowRealParam.extend(self.firstMoreRealParam)
        self.FollowValueParam.extend(self.FollowRealParam)
        self.FollowMoreRealParam.extend(self.FollowParamListInFuncProc)
    

    def letsWork(self):
        self.starSyntaticAnalyzer()
        self.writeFiles()


    def starSyntaticAnalyzer(self):
        self.getNextToken()
        self.start()
       
        
    def getNextToken(self):
        if self.currentToken >= len(self.listTokens):
            self.lexemToken = None
        else:
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
        self.creat_functionProcedures_TB()
        self.back_to_begin()
        self.getNextToken()
        self.callGlobalValues()
        self.callFunctionProcedure()
        self.semantic.print_semantic_errors()
    
    def creat_functionProcedures_TB(self):
        while (not(self.lexemToken == None)):
            if (not(self.lexemToken in self.firstFunctions_Procedures)):
                self.getNextToken()
            else:
                if self.lexemToken == "function":
                    self.getNextToken()

                    typeFunction = ""
                    if self.lexemToken in self.firstType:
                        typeFunction = self.lexemToken
                        self.getNextToken()
                    
                    functionName = ""
                    line = ""
                    if self.typeLexema == "IDE":
                        functionName =  self.lexemToken
                        line = self.errorLineToken
                        self.getNextToken()

                    if self.lexemToken == "(":
                        self.getNextToken()

                    type_params = []
                    params = []
                    if self.lexemToken in self.firstParamList:
                        type_params, params = self.readParamList_TB(functionName, type_params, params)

                    if self.lexemToken == ")":
                        self.getNextToken()

                    self.semantic.add_func(functionName, typeFunction, type_params, params, line)


                elif self.lexemToken == "procedure":
                    self.getNextToken()
                    
                    procedureName = ""
                    line = ""
                    if self.typeLexema == "IDE" or self.lexemToken == "start":
                        procedureName =  self.lexemToken
                        line = self.errorLineToken
                        self.getNextToken()

                    if self.lexemToken == "(":
                        self.getNextToken()

                    type_params = []
                    params = []
                    if self.lexemToken in self.firstParamList:
                        type_params, params = self.readParamList_TB(procedureName, type_params, params)

                    if self.lexemToken == ")":
                        self.getNextToken()

                    self.semantic.add_func(procedureName, None, type_params, params, line)

        #CHAMADA PARA VERIFICAÇÃO DO START
        self.semantic.check_start()


    def readParamList_TB(self, escopo, type_params, params):
        type_param = ""
        param = ""
        line = ""
        if self.lexemToken in self.firstType:
            type_param = self.lexemToken
            type_params.append(self.lexemToken)
            self.getNextToken()

        if self.typeLexema == "IDE":
            param = self.lexemToken
            params.append(self.lexemToken)
            line = self.errorLineToken
            self.getNextToken()
        
        self.semantic.add_var(escopo, type_param, param, None, line)

        if self.lexemToken == ",":
            self.getNextToken()
            self.readParamList_TB(escopo, type_params, params)
        
        return type_params, params


    def back_to_begin(self):
        self.currentToken = 0
        self.previousToken = 0
        self.numberFile = 0
        self.lexemToken = ""
        self.typeLexema = ""
        self.typeNRO = ""
        self.errorLineToken = 0
    
    def callGlobalValues(self):
        if self.lexemToken in self.firstGlobalValues:
            if self.lexemToken == "const":
                self.getNextToken()
                
                if self.lexemToken == "{":
                    self.getNextToken()
                else:
                    while not ((self.lexemToken == "{") or (self.lexemToken in self.firstConstValuesDeclaration) or (self.lexemToken in self.FollowGlobalValeus)) and not(self.lexemToken == None):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["{"]))
                        self.getNextToken()
                    if (not self.lexemToken == "{"):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
                    elif (self.lexemToken == "{"):
                        self.getNextToken()
                
                self.callConstValuesDeclaration("global_const")
                
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
                    
                self.callVarValuesDeclaration("global_var")
                
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
                
                self.callVarValuesDeclaration("global_var")
                
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
                
                self.callConstValuesDeclaration("global_const")
                
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
                
    
    def callConstValuesDeclaration(self, escopo):
        if self.lexemToken in self.firstConstValuesDeclaration:
            typeConst = self.lexemToken
            self.getNextToken()
            
            self.callConstValuesAttribution(escopo, typeConst)
            self.callConstMoreAttributions(escopo, typeConst)
            
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

            self.callConstValuesDeclaration(escopo)

        else:
            while (not ((self.lexemToken in self.firstConstValuesDeclaration) or (self.lexemToken in self.FollowConstValuesDeclaration)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FollowConstValuesDeclaration))
                self.getNextToken()

            if self.lexemToken in self.firstConstValuesDeclaration:
                self.callConstValuesDeclaration(escopo)
            else:
                pass
 
        
    def callConstValuesAttribution(self, escopo, typeConst):
        if self.typeLexema in self.firstConstValuesAttribution:
            nameConst = self.lexemToken
            line = self.errorLineToken
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
            valorConst = self.lexemToken
            self.getNextToken()
            self.semantic.add_var(escopo, typeConst, nameConst, valorConst, line)

        else:
            while(not((self.lexemToken in self.firstValueConst or self.typeLexema in self.firstValueConst) or (self.lexemToken in self.FollowConstValuesAttribution)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstValueConst))
                self.getNextToken()
            if (not (self.lexemToken in self.firstValueConst or self.typeLexema in self.firstValueConst)):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "valor", ""))
            elif (self.lexemToken in self.firstValueConst or self.typeLexema in self.firstValueConst):
                self.getNextToken()  
    
    
    def callConstMoreAttributions(self, escopo, typeConst):
        if self.lexemToken in self.firstVarMoreAttributions:
            self.getNextToken()
            self.callConstValuesAttribution
            self.callConstMoreAttributions

        else:
            while(not((self.lexemToken in self.firstConstMoreAttributions) or (self.lexemToken in self.FollowConstMoreAttributions)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FollowConstMoreAttributions))
                self.getNextToken()
            if self.lexemToken in self.firstConstMoreAttributions:
                self.callConstMoreAttributions(escopo, typeConst)
        

    def callVarValuesDeclaration_Struct(self, type_atrributes, atrributes, tipo_array, ide_array, size1_array, size2_array, size3_array, line): #FUNÇAO PRA TRATAMENTO DOS ATRIBUTOS DE STRUCTS
        if self.lexemToken in self.firstVarValuesDeclaration:
            if self.lexemToken in self.firstType:
                type_atrributes.append(self.lexemToken)

                self.getNextToken()
                self.callVarValuesAttribution_Struct(type_atrributes, atrributes, tipo_array, ide_array, size1_array, size2_array, size3_array, line)
                self.callVarMoreAttributions_Struct(type_atrributes, atrributes, tipo_array, ide_array, size1_array, size2_array, size3_array, line)
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
                    
                self.callVarValuesDeclaration_Struct(type_atrributes, atrributes, tipo_array, ide_array, size1_array, size2_array, size3_array, line)
        
        return type_atrributes, atrributes, tipo_array, ide_array, size1_array, size2_array, size3_array, line


    def callVarValuesAttribution_Struct(self, type_atrributes, atrributes, tipo_array, ide_array, size1_array, size2_array, size3_array, line): #NECESSITA MODIFICAR
        if self.typeLexema in self.firstVarValuesAttribution:
            atrributes.append(self.lexemToken)
            line = self.errorLineToken
            self.getNextToken()
        else:
            while (not ((self.typeLexema == "IDE") or (self.lexemToken in self.firstArrayVerification) or (self.lexemToken in self.FollowVarValuesAttribution)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["IDE"]))
                self.getNextToken()
            if (not self.typeLexema == "IDE"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
            elif (self.typeLexema == "IDE"):
                self.getNextToken()
        
        arrayControl = False
        sizeArray = []

        if self.lexemToken in self.firstArrayVerification:
            arrayControl = True
            sizeArray = self.callArrayVarification(sizeArray)

        if (arrayControl == True):
            tipo_array.append(type_atrributes[len(type_atrributes) - 1]) #Coloca o tipo na lista de array
            type_atrributes.pop(len(type_atrributes) - 1) #Remove o tipo da lista de variaveis

            ide_array.append(atrributes[len(atrributes) - 1]) #Coloca o nome na lista de array
            atrributes.pop(len(atrributes) - 1) #Remove o nome da lista de variaveis

            size1_array.append(sizeArray[0])
            size2_array.append(sizeArray[1])
            size3_array.append(sizeArray[2])
        else:
            pass
    

    def callVarMoreAttributions_Struct(self, type_atrributes, atrributes, tipo_array, ide_array, size1_array, size2_array, size3_array, line): #MODIFICAR
        if self.lexemToken in self.firstVarMoreAttributions:
            self.getNextToken()
            self.callVarValuesAttribution_Struct(type_atrributes, atrributes, tipo_array, ide_array, size1_array, size2_array, size3_array, line)
            self.callVarMoreAttributions_Struct(type_atrributes, atrributes, tipo_array, ide_array, size1_array, size2_array, size3_array, line)


    def callVarValuesDeclaration(self, escopo):
        if self.lexemToken in self.firstVarValuesDeclaration:
            if self.lexemToken in self.firstType:
                typeVar = self.lexemToken

                self.getNextToken()
                self.callVarValuesAttribution(escopo, typeVar)
                self.callVarMoreAttributions(escopo, typeVar)
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
                    
                self.callVarValuesDeclaration(escopo)
                
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
                
                self.callIDE_Struct(escopo)
                self.callVarValuesDeclaration(escopo)
                
            elif self.lexemToken == "struct":
                self.getNextToken()
                self.callIDE_Struct(escopo)
                self.callVarValuesDeclaration(escopo)

        else:
            while (not (self.lexemToken in self.firstVarValuesDeclaration or self.lexemToken in self.FollowVarValuesDeclaration) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FollowVarValuesDeclaration))
                self.getNextToken()
            if self.lexemToken in self.firstVarValuesDeclaration:
                self.callVarValuesDeclaration(escopo)
            else:
                pass

            
    def callVarValuesAttribution(self, escopo, typeVar):
        if self.typeLexema in self.firstVarValuesAttribution:
            nameVar = self.lexemToken
            line = self.errorLineToken
            self.getNextToken()
        else:
            while (not ((self.typeLexema == "IDE") or (self.lexemToken in self.firstArrayVerification) or (self.lexemToken in self.FollowVarValuesAttribution)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["IDE"]))
                self.getNextToken()
            if (not self.typeLexema == "IDE"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
            elif (self.typeLexema == "IDE"):
                self.getNextToken()
        
        arrayControl = False
        sizeArray = []

        if self.lexemToken in self.firstArrayVerification:
            arrayControl = True
            sizeArray = self.callArrayVarification(sizeArray)

        if (arrayControl == True):
            i = len(sizeArray)
            sizeArray1 = '0'
            sizeArray2 = '0'
            sizeArray3 = '0'
            if (i > 0):
                sizeArray1 = str(sizeArray[i-1])
                i = i - 1
                if (i > 0):
                    sizeArray2 = str(sizeArray[i-1])
                    i = i - 1
                    if (i > 0):
                        sizeArray3 = str(sizeArray[i-1])

            self.semantic.add_array(escopo,typeVar,nameVar,sizeArray1,sizeArray2,sizeArray3, line)
        else:
            self.semantic.add_var(escopo, typeVar, nameVar, None, line)
            
    def callArrayVarification(self, sizeArray): 
        if self.lexemToken in self.firstArrayVerification:
            self.getNextToken()
            if self.typeNRO == "NRO_I":
                sizeArray.append(self.lexemToken)
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
            
            if self.lexemToken in self.firstArrayVerification:
                self.callArrayVarification(sizeArray)

        else:
            while(not((self.lexemToken in self.firstArrayVerification) or (self.lexemToken in self.FollowArrayVerification)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstArrayVerification))
                self.getNextToken()
            if self.lexemToken in self.firstArrayVerification:
                self.callArrayVarification(sizeArray)
            else:
                pass

        return sizeArray
    

    def callVarMoreAttributions(self, escopo, typeVar):
        if self.lexemToken in self.firstVarMoreAttributions:
            self.getNextToken()
            self.callVarValuesAttribution(escopo, typeVar)
            self.callVarMoreAttributions(escopo, typeVar)
        else:
            while(not((self.lexemToken in self.firstVarMoreAttributions) or (self.lexemToken in self.FollowVarMoreAttributions)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.FollowVarMoreAttributions))
                self.getNextToken()

        

    def callIDE_Struct(self, escopo):
        if self.typeLexema in self.firstIDE_Struct:
            nameStruct = self.lexemToken
            lineStruct = self.errorLineToken
            self.getNextToken()
        else:
            while(not((self.typeLexema in self.firstIDE_Struct) or (self.lexemToken in self.firstIDE_Struct2 or self.typeLexema in self.firstIDE_Struct2) or (self.lexemToken in self.FollowIDE_Struct)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstIDE_Struct))
                self.getNextToken()
            if (not (self.typeLexema == "IDE")):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
            elif (self.typeLexema == "IDE"):
                self.getNextToken()
        
        self.callIDE_Struct2(escopo, nameStruct, lineStruct)
        
        
    def callIDE_Struct2(self, escopo, nameStruct, line):
        name_extends = ""
        if self.lexemToken in self.firstIDE_Struct2:
            if self.lexemToken == "{":
                self.callIDE_Struct2Aux(escopo, nameStruct, None, line)

            elif self.lexemToken == "extends":
                self.getNextToken()

                if self.typeLexema == "IDE":
                    name_extends = self.lexemToken
                    self.getNextToken()
                else:
                    while(not((self.typeLexema == "IDE") or (self.lexemToken in self.firstIDE_Struct2Aux) or (self.lexemToken in self.FollowIDE_Struct)) and (not self.lexemToken == None)):
                        self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["IDE"]))
                        self.getNextToken()
                    if (not (self.typeLexema == "IDE")):
                        self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
                    elif (self.typeLexema == "IDE"):
                        self.getNextToken()

                self.callIDE_Struct2Aux(escopo, nameStruct, name_extends, line)
        
        else:
            while(not((self.lexemToken in self.firstIDE_Struct2) or (self.lexemToken in self.FollowIDE_Struct2)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstIDE_Struct2))
                self.getNextToken()
            if self.lexemToken in self.firstIDE_Struct2:
                self.callIDE_Struct2(escopo, nameStruct, line)
            else:
                pass

    
    def callIDE_Struct2Aux(self, escopo, nameStruct, name_extends, line):
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
        
        type_atrributes = []
        atrributes = []
        tipo_array = []
        ide_array = []
        size1_array = []
        size2_array = []
        size3_array = []
        type_atrributes, atrributes, tipo_array, ide_array, size1_array, size2_array, size3_array, line = self.callVarValuesDeclaration_Struct(type_atrributes, atrributes, tipo_array, ide_array, size1_array, size2_array, size3_array, line) #FUNÇÃO INCOMPLETA, EM MODIFICAÇÃO
        type_atrributes.extend(tipo_array)
        atrributes.extend(ide_array)

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

        self.semantic.add_struct(nameStruct, escopo, type_atrributes, atrributes, name_extends, line) #ALTERAR NO SEMANTICO

            
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

        functionName = ""
        if self.typeLexema == "IDE":
            functionName =  self.lexemToken
            self.getNextToken()
        else:
            while (not ((self.typeLexema == "IDE" or self.lexemToken == "start") or (self.lexemToken == "(") or (self.lexemToken in self.FollowFunction)) and (not self.lexemToken == None)):
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

        if self.lexemToken in self.firstParamList:
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

        self.callVarFunctionsProcedures(functionName)
        if self.lexemToken in self.firstCommand or self.typeLexema in self.firstCommand:
            self.callCommands(functionName)           
          
        self.callReturn(functionName)

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
        procedureName = ""
        if self.typeLexema == "IDE" or self.lexemToken == "start":
            procedureName = self.lexemToken
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

        if self.lexemToken in self.firstParamList:
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

        self.callVarFunctionsProcedures(procedureName)
        
        if self.lexemToken in self.firstCommand or self.typeLexema in self.firstCommand:
            self.callCommands(procedureName)

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
        if self.lexemToken in self.firstType:
            if self.lexemToken in self.firstType:
                self.getNextToken()
            else:
                while (not ((self.lexemToken in self.firstType) or (self.typeLexema == "IDE") or (self.lexemToken in self.FollowParamList)) and (not self.lexemToken == None)):
                    self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstType))
                    self.getNextToken()
                if (not self.lexemToken in self.firstType):
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "tipo", ""))
                elif (self.lexemToken in self.firstType):
                    self.getNextToken()
            
            if self.typeLexema == "IDE":
                self.getNextToken()
            else:
                while (not ((self.typeLexema == "IDE") or (self.lexemToken in self.firstMoreParam) or (self.lexemToken in self.FollowParamList)) and (not self.lexemToken == None)):
                    self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstType))
                    self.getNextToken()
                if (not self.typeLexema == "IDE"):
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
                elif (self.typeLexema == "IDE"):
                    self.getNextToken()
            
            if self.lexemToken in self.firstMoreParam:
                self.callMoreParam()

        else:
            while (not ((self.lexemToken in self.firstType) or (self.lexemToken in self.FollowParamList)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstType))
                self.getNextToken()
            if (self.lexemToken in self.firstType):
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

    
    def callParamListInFuncProc(self, name_params, type_token_params):
        if (self.typeLexema == "IDE"):
            name_params.append(self.lexemToken)
            type_token_params.append(self.typeLexema)

        elif (self.typeLexema == "NRO"):
            name_params.append(self.lexemToken)
            type_token_params.append(self.typeLexema)


        elif (self.typeLexema == "CDC"):
            name_params.append(self.lexemToken)
            type_token_params.append(self.typeLexema)

        elif (self.typeLexema == "PRE" and (self.lexemToken == "true" or self.lexemToken == "false")):
            name_params.append(self.lexemToken)
            type_token_params.append(self.typeLexema)

        self.getNextToken()

        if (self.lexemToken == ","):
            self.getNextToken()
            self.callParamListInFuncProc(name_params, type_token_params)

        return name_params, type_token_params


    def callVarFunctionsProcedures(self, escopo):
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
        
        self.callVarValuesDeclaration(escopo)

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

    
    def callCommands(self, escopo):
        if self.lexemToken in self.firstCommand or self.typeLexema in self.firstCommand:
            self.callCommand(escopo)
            if self.lexemToken in self.firstCommands:
                self.callCommands(escopo)

        else:
            while (not ((self.lexemToken in self.firstCommand) or (self.typeLexema in self.firstCommand) or (self.lexemToken in self.FollowCommand)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstCommand))
                self.getNextToken()
            if self.lexemToken in self.firstCommand or self.typeLexema in self.firstCommand:
                self.callCommands(escopo)


    def callCommand(self, escopo):
        if self.lexemToken in self.firstCommandIf:
            self.callIfStatement(escopo)

        elif self.lexemToken in self.firstCommandWhile:
            self.callWhileStatement(escopo)

        elif self.lexemToken in self.firstCommandRead:
            self.callReadStatement(escopo)

        elif self.lexemToken in self.firstCommandPrint:
            self.calPrintStatement(escopo)

        elif self.lexemToken in self.firstAssignment or self.typeLexema in self.firstAssignment:
            self.callAssignment(escopo)

        elif self.typeLexema in self.firstCallProcedure_Function:
            self.callCallProcedureFunction(escopo)            

    
    def callIfStatement(self, escopo):
        if self.lexemToken in self.firstCommandIf:
            self.getNextToken()
        else:
            while (not ((self.lexemToken in self.firstCommandIf) or (self.lexemToken == "(") or (self.lexemToken in self.FollowCommandIf)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstCommandIf))
                self.getNextToken()
            if (not self.lexemToken in self.firstCommandIf):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "if"))
            elif (self.lexemToken in self.firstCommandIf):
                self.getNextToken()
        
        if self.lexemToken == '(':
            self.getNextToken()            
        else:
            while (not ((self.lexemToken == "(") or (self.lexemToken in self.firstRelacionalExp) or (self.lexemToken in self.FollowCommandIf)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["("]))
                self.getNextToken()
            if (not self.lexemToken == "("):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "("))
            elif (self.lexemToken == "("):
                self.getNextToken()
        
        self.callRelationalExp(escopo)

        if self.lexemToken == ')':
            self.getNextToken()
        else:
            while (not ((self.lexemToken == ")") or (self.lexemToken == "then") or (self.lexemToken in self.FollowCommandIf)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, [")"]))
                self.getNextToken()
            if (not self.lexemToken == ")"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ")"))
            elif (self.lexemToken == ")"):
                self.getNextToken()
        
        if self.lexemToken == 'then':
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "then") or (self.lexemToken == "{") or (self.lexemToken in self.FollowCommandIf)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["then"]))
                self.getNextToken()
            if (not self.lexemToken == "then"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "then"))
            elif (self.lexemToken == "then"):
                self.getNextToken()
        
        if self.lexemToken == '{':
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "{") or (self.lexemToken in self.firstCommands) or (self.lexemToken in self.FollowCommandIf)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["{"]))
                self.getNextToken()
            if (not self.lexemToken == "{"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
            elif (self.lexemToken == "{"):
                self.getNextToken()

        if self.lexemToken in self.firstCommand or self.typeLexema in self.firstCommand:
            self.callCommands(escopo)
        
        if self.lexemToken == '}':
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "}") or (self.lexemToken in self.FollowCommandIf)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["}"]))
                self.getNextToken()
            if (not self.lexemToken == "}"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
            elif (self.lexemToken == "}"):
                self.getNextToken()
        
        if self.lexemToken == "else":
            self.callElseStatement(escopo)

    
    def callElseStatement(self, escopo):
        self.getNextToken()
        
        if self.lexemToken == "{":
            self.getNextToken()
        else:
          pass  
        
        if self.lexemToken in self.firstCommands or self.typeLexema in self.firstCommand:
            self.callCommands(escopo)
            
        if self.lexemToken == "}":
            self.getNextToken()
        else:
          pass  
    
    def callWhileStatement(self, escopo):
        if self.lexemToken in self.firstCommandWhile:
            self.getNextToken()
        else:
            while (not ((self.lexemToken in self.firstCommandWhile) or (self.lexemToken == "(") or (self.lexemToken in self.FollowCommandWhile)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstCommandWhile))
                self.getNextToken()
            if (not self.lexemToken in self.firstCommandWhile):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "while"))
            elif (self.lexemToken in self.firstCommandWhile):
                self.getNextToken()
        
        if self.lexemToken == '(':
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "(") or (self.lexemToken in self.firstRelacionalExp) or (self.lexemToken in self.FollowCommandWhile)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["("]))
                self.getNextToken()
            if (not self.lexemToken == "("):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "("))
            elif (self.lexemToken == "("):
                self.getNextToken()

        self.callRelationalExp(escopo)
        
        if self.lexemToken == ')':
            self.getNextToken()
        else:
            while (not ((self.lexemToken == ")") or (self.lexemToken == "{") or (self.lexemToken in self.FollowCommandWhile)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, [")"]))
                self.getNextToken()
            if (not self.lexemToken == ")"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ")"))
            elif (self.lexemToken == ")"):
                self.getNextToken()
        
        if self.lexemToken == '{':
            self.getNextToken()
        else: 
            while (not ((self.lexemToken == "{") or (self.lexemToken in self.firstCommands) or (self.lexemToken in self.FollowCommandWhile)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["{"]))
                self.getNextToken()
            if (not self.lexemToken == "{"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "{"))
            elif (self.lexemToken == "{"):
                self.getNextToken()

        if self.lexemToken in self.firstCommand or self.typeLexema in self.firstCommand:
            self.callCommands(escopo)
        
        if self.lexemToken == '}':
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "}") or (self.lexemToken in self.FollowCommandWhile)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["}"]))
                self.getNextToken()
            if (not self.lexemToken == "}"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "}"))
            elif (self.lexemToken == "}"):
                self.getNextToken()

    
    def callReadStatement(self, escopo):
        if self.lexemToken in self.firstCommandRead:
            self.getNextToken()
        else:
            while (not ((self.lexemToken in self.firstCommandIf) or (self.lexemToken == "(") or (self.lexemToken in self.FollowCommandRead)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstCommandRead))
                self.getNextToken()
            if (not self.lexemToken in self.firstCommandRead):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "read"))
            elif (self.lexemToken in self.firstCommandRead):
                self.getNextToken()
        
        if self.lexemToken == "(":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "(") or (self.lexemToken in self.firstReadParam) or (self.lexemToken in self.FollowCommandRead)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["("]))
                self.getNextToken()
            if (not self.lexemToken == "("):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "("))
            elif (self.lexemToken == "("):
                self.getNextToken()
        
        self.callReadParam(escopo)

        if self.lexemToken == ")":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == ")") or (self.lexemToken == ";") or (self.lexemToken in self.FollowCommandRead)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, [")"]))
                self.getNextToken()
            if (not self.lexemToken == ")"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ")"))
            elif (self.lexemToken == ")"):
                self.getNextToken()
        
        if self.lexemToken == ";":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == ";") or (self.lexemToken in self.FollowCommandRead)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, [";"]))
                self.getNextToken()
            if (not self.lexemToken == ";"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ";"))
            elif (self.lexemToken == ";"):
                self.getNextToken()


    def callReadParam(self, escopo):
        if self.lexemToken in self.firstReadParam:
            real_escopo = ""
            variable = ""
            structs_name = ""
            array_size = []
            line = self.errorLineToken
            real_escopo, variable, structs_name, array_size = self.callCallVariable(escopo, real_escopo, variable, structs_name, array_size)
            self.semantic.check_read_print(real_escopo, variable, structs_name, array_size, line)
            if self.lexemToken in self.firstMoreReadParams:
                self.callMoreReadParams(escopo)
        else:
            while (not ((self.lexemToken in self.firstReadParam) or (self.lexemToken in self.FollowReadParam)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstReadParam))
                self.getNextToken()
            if (not self.lexemToken in self.firstReadParam):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "parametros", "R"))
            elif (self.lexemToken in self.firstReadParam):
                self.callReadParam(escopo)

    
    def callMoreReadParams(self, escopo):
        if self.lexemToken in self.firstMoreReadParams:
            self.getNextToken()
            self.callReadParam(escopo)
        else:
            while (not ((self.lexemToken in self.firstMoreReadParams) or (self.lexemToken in self.FollowMoreReadParams)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstMoreReadParams))
                self.getNextToken()
            if (not self.lexemToken in self.firstMoreReadParams):
                self.callMoreReadParams
            elif (self.lexemToken in self.FollowMoreReadParams):
                pass


    def calPrintStatement(self, escopo):
        if self.lexemToken in self.firstCommandPrint:
            self.getNextToken()
        else:
            while (not ((self.lexemToken in self.firstCommandRead) or (self.lexemToken == "(") or (self.lexemToken in self.FollowCommandPrint)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstCommandPrint))
                self.getNextToken()
            if (not self.lexemToken in self.firstCommandPrint):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "palavra", "print"))
            elif (self.lexemToken in self.firstCommandPrint):
                self.getNextToken()
        
        if self.lexemToken == "(":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "(") or (self.lexemToken in self.firstPrintParams) or (self.lexemToken in self.FollowCommandPrint)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["("]))
                self.getNextToken()
            if (not self.lexemToken == "("):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "("))
            elif (self.lexemToken == "("):
                self.getNextToken()
        
        self.callPrintParams(escopo)

        if self.lexemToken == ")":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == ")") or (self.lexemToken == ";") or (self.lexemToken in self.FollowCommandPrint)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, [")"]))
                self.getNextToken()
            if (not self.lexemToken == ")"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ")"))
            elif (self.lexemToken == ")"):
                self.getNextToken()
        
        if self.lexemToken == ";":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == ";") or (self.lexemToken in self.FollowCommandPrint)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, [";"]))
                self.getNextToken()
            if (not self.lexemToken == ";"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ";"))
            elif (self.lexemToken == ";"):
                self.getNextToken()


    def callPrintParams(self, escopo):
        if self.lexemToken in self.firstPrintParams or self.typeLexema in self.firstPrintParams:
            self.callPrintParam(escopo)
            
            if self.lexemToken in self.firstMorePrintParams:
                self.callMorePrintParams(escopo)
        else:
            while (not ((self.lexemToken in self.firstPrintParams) or (self.lexemToken in self.FollowPrintParams)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstPrintParam))
                self.getNextToken()
            if (not self.lexemToken in self.firstPrintParams):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "parametros", "P"))
            elif (self.lexemToken in self.firstPrintParams):
                self.callPrintParams(escopo)


    def callPrintParam(self, escopo):
        if self.lexemToken in self.firstPrintParam or self.typeLexema in self.firstPrintParam:
            if (self.typeLexema == "CDC"):
                self.getNextToken()
            elif (self.lexemToken in self.firstCallVariable):
                real_escopo = ""
                variable = ""
                structs_name = ""
                array_size = []
                line = self.errorLineToken
                real_escopo, variable, structs_name, array_size = self.callCallVariable(escopo, real_escopo, variable, structs_name, array_size)
                self.semantic.check_read_print(real_escopo, variable, structs_name, array_size, line)
        else:
            while (not ((self.lexemToken in self.firstPrintParam) or (self.lexemToken in self.FollowPrintParam)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstPrintParam))
                self.getNextToken()
            if (not self.lexemToken in self.firstPrintParam):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "parametros", "P"))
            elif (self.lexemToken in self.firstPrintParam):
                self.callPrintParam(escopo)   


    def callMorePrintParams(self, escopo):
        if (self.lexemToken in self.firstMorePrintParams):
            self.getNextToken()
            self.callPrintParams(escopo)
        else:
            while (not ((self.lexemToken in self.firstMorePrintParams) or (self.lexemToken in self.FollowMorePrintParams)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstMorePrintParams))
                self.getNextToken()
            if (self.lexemToken in self.firstMorePrintParams):
                self.callMorePrintParams(escopo)


    def callAssignment(self, escopo):
        if self.lexemToken in self.firstCallVariable:
            variable = [0]
            variable= ""
            real_escopo = ""
            structs_name = ""
            array_size = []
            line = self.errorLineToken
            real_escopo, variable, structs_name, array_size = self.callCallVariable(escopo, real_escopo, variable, structs_name, array_size)
            #CHAMAR VERIFICAÇÃO DE ERRO SEMÂNTICO AQUI
            if self.lexemToken == '=':
                self.getNextToken()
            else:
                while (not ((self.lexemToken == "=") or (self.typeLexema in self.firstAssign2 or self.lexemToken in self.firstAssign2) or (self.lexemToken in self.FollowAssignment)) and (not self.lexemToken == None)):
                    self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["="]))
                    self.getNextToken()
                if (not self.lexemToken == "="):
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "="))
                elif (self.lexemToken == "="):
                    self.getNextToken()

            tipo_assign = ""
            value = ""
            escopo2 = ""
            values_struct_left = []
            values_struct_right = []
            if (self.lexemToken in self.firstAssign2 or self.typeLexema in self.firstAssign2):
                tipo_assign, value, escopo2, values_struct_right = self.callAssign2(escopo, tipo_assign, value, escopo2, values_struct_right)
            else:
                pass

            # VER COMO FICARÁ TRATAMENTO DE STRUCT
            if ((len(array_size) > 0) and structs_name == ""):
                if (len(values_struct_right)>0):
                    self.semantic.assign_array(variable,real_escopo,values_struct_right,escopo2, tipo_assign,line)
                else:
                    self.semantic.assign_array(variable,real_escopo,value,escopo2, tipo_assign,line)
            
            elif ((len(array_size) == 0) and structs_name == ""):
                if (len(values_struct_right)>0):
                    self.semantic.assign_var(variable,real_escopo,values_struct_right,escopo2,tipo_assign,line)
                else:
                    self.semantic.assign_var(variable,real_escopo,value,escopo2,tipo_assign,line)
            
            else:
                values_struct_left.append(variable)
                values_struct_left.append(structs_name)
                if (len(values_struct_right) > 0):
                    self.semantic.assign_struct(values_struct_left, real_escopo, values_struct_right, escopo2, tipo_assign, line)
                else:
                    self.semantic.assign_struct(values_struct_left, real_escopo, value, escopo2, tipo_assign, line)
                
            
            if self.lexemToken == ';':
                self.getNextToken()
            else:
                while (not ((self.lexemToken == ";") or  (self.lexemToken in self.FollowAssignment)) and (not self.lexemToken == None)):
                    self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, [";"]))
                    self.getNextToken()
                if (not self.lexemToken == ";"):
                    self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ";"))
                elif (self.lexemToken == ";"):
                    self.getNextToken()

        elif self.lexemToken in self.firstUnaryOP:
            self.callUnaryOp(escopo)
        else:
            pass

    
    def callAssign2(self, escopo, tipo_assign, value, escopo2, values_struct_right):
        if self.typeLexema in self.firstCallProcedure_Function:
            tipo_assign = 'func'
            value = self.lexemToken
            self.callCallProcedureFunction(escopo)
        
        elif self.lexemToken in self.firstModifier:
            variable = ""
            real_escopo = ""
            structs_name = ""
            array_size = []
            real_escopo, variable, structs_name, array_size = self.callCallVariable(escopo, real_escopo, variable, structs_name, array_size)

            if (len(array_size) > 0) and structs_name == "":
                tipo_assign = 'array'
                value = variable
                escopo2 = real_escopo
            elif (len(array_size) == 0) and structs_name == "":
                tipo_assign = 'variavel'
                value = variable
                escopo2 = real_escopo
            elif (len(structs_name) > 0):
                tipo_assign = 'struct'
                escopo2 = real_escopo
                values_struct_right.append(variable)
                values_struct_right.append(structs_name)

        elif self.lexemToken in self.firstExpression:
            self.callExpression(escopo)
        
        elif self.typeLexema == 'CDC':
            tipo_assign = 'primitivo'
            value = self.lexemToken
            self.getNextToken()
        
        elif self.typeLexema == "NRO":
            tipo_assign = 'primitivo'
            value = self.lexemToken
            self.getNextToken()
        
        else:
            pass

        return tipo_assign, value, escopo2, values_struct_right


    def callStruct(self, escopo, structs_name, array_size):
        if self.lexemToken == '.':
            self.getNextToken()
        else:
            while (not ((self.lexemToken == ".") or (self.typeLexema == "IDE") or (self.lexemToken in self.FollowStruct)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["."]))
                self.getNextToken()
            if (not self.lexemToken == "."):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "."))
            elif (self.lexemToken == "."):
                self.getNextToken()

        if self.typeLexema == 'IDE':
            structs_name = self.lexemToken
            self.getNextToken()
        else:
            while (not ((self.typeLexema == "IDE") or (self.lexemToken in self.firstPaths) or (self.lexemToken in self.FollowStruct)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["IDE"]))
                self.getNextToken()
            if (not self.typeLexema == "IDE"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
            elif (self.typeLexema == "IDE"):
                self.getNextToken()

        if self.lexemToken in self.firstPaths:
            self.callPaths(escopo, structs_name, array_size)
        else:
            pass
        
        return structs_name, array_size


    def callPaths(self, escopo, structs_name, array_size):
        if self.lexemToken == '.':
            structs_name, array_size = self.callStruct(escopo, structs_name, array_size)
        
        elif self.lexemToken in self.firstMatrAssign:
            structs_name, array_size = self.callMatrAssign(escopo, structs_name, array_size)

        return structs_name, array_size
        

    def callMatrAssign(self, escopo, structs_name, array_size):
        if self.lexemToken == '[':
            array_size = self.callCell(escopo, array_size)
        else:
            pass
        if self.lexemToken in self.firstPaths:
            structs_name, array_size = self.callPaths(escopo, structs_name, array_size)
        else:
            pass

        return structs_name, array_size


    def callCell(self, escopo, array_size):
        if self.lexemToken == ('['):
            self.getNextToken()
            if self.typeLexema == 'NRO':
                array_size.append(self.lexemToken)
                self.getNextToken()
            else:
                pass
            if self.lexemToken == ']':
                self.getNextToken()
            else:
                pass

        elif self.lexemToken == ('['):
            self.getNextToken()
            if self.typeLexema in self.firstCallVariable:
                real_escopo = ""
                variable = ""
                structs_name = ""
                array_size = []
                line = self.errorLineToken
                real_escopo, variable, structs_name, array_size = self.callCallVariable(escopo, real_escopo, variable, structs_name, array_size)
                self.semantic.check_read_print(real_escopo, variable, structs_name, array_size, line)
            else:
                pass
            if self.lexemToken == ']':
                self.getNextToken()
            else:
                pass
        else:
            pass

        return array_size

    
    def callCallProcedureFunction(self, escopo): ##
        nameFP = ""
        line = ""
        if (self.typeLexema == "IDE"):
            nameFP = self.lexemToken
            line = self.errorLineToken
            self.getNextToken()
        else:
            pass

        if self.lexemToken == "(":
            self.getNextToken()
        else:
            while (not ((self.lexemToken == "(") or (self.lexemToken in self.firstParamListInFuncProc) or (self.lexemToken in self.FollowCallProcedureFunction)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["("]))
                self.getNextToken()
            if (not self.lexemToken == "("):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "("))
            elif (self.lexemToken == "("):
                self.getNextToken()

        name_params = []
        type_tokens_params = []
        if self.lexemToken in self.firstParamListInFuncProc or self.typeLexema in self.firstParamListInFuncProc:
            name_params, type_tokens_params = self.callParamListInFuncProc(name_params, type_tokens_params)

        if (self.lexemToken == ")"):
            self.getNextToken()
        else:
            while (not ((self.lexemToken == ")") or (self.lexemToken == ";") or (self.lexemToken in self.FollowCallProcedureFunction)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, [")"]))
                self.getNextToken()
            if (not self.lexemToken == ")"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ")"))
            elif (self.lexemToken == ")"):
                self.getNextToken()

        self.semantic.call_func(escopo, nameFP, name_params, type_tokens_params, line)


    def callComandsExp(self, escopo):
        if self.lexemToken in self.firstAritmeticExp:
                self.callRelationalExp(escopo)
        elif self.lexemToken in self.firstLogicalOperators:
             self.callOptLogicalExp(escopo)
        else:
            pass        

    
    def callExpression(self, escopo):
        if self.lexemToken in self.firstLogicalExp:
                self.callLogicalExp(escopo)
        elif self.lexemToken in self.firstAritmeticExp:
            self.callAritmeticExp(escopo)
        else:
            pass


    def callRelationalExp(self, escopo):
        if self.lexemToken in self.firstAritmeticExp:
            self.callAritmeticExp(escopo)
            if self.lexemToken in self.firstPossRelExp:
                self.callPosRelExp(escopo)
            else:
                pass    
        
        elif self.lexemToken == '(':
            self.getNextToken
            if self.lexemToken in self.firstLogicalExp:
                self.callLogicalExp(escopo)
            else:
                pass
            if self.getNextToken == ')':
                self.getNextToken()
            else:
                pass
        else:
            pass


    def callOptLogicalExp(self, escopo):
        if self.lexemToken in self.firstLogicalOperators:
                self.getNextToken()
        else:
            pass
        if self.lexemToken in self.firstLogicalExp:
                self.callLogicalExp(escopo)
        else:
            pass
        

    def callLogicalExp(self, escopo):
        if self.lexemToken in self.firstAritmeticExp:
            self.callRelationalExp(escopo)
        else:
            pass
        if self.lexemToken in self.firstLogicalOperators:
             self.callOptLogicalExp(escopo)
        else:
            pass        


    def callPosRelExp(self, escopo):
        if self.lexemToken in self.firstRelationalLessPrec:
            self.getNextToken()
            if self.lexemToken in self.firstAritmeticExp:
                self.callAritmeticExp(escopo)
            else:
                pass
            if self.lexemToken in self.firstRelationalMorePrec:
                self.callInequalityExp(escopo)
            else:
                pass
            if self.lexemToken in self.firstRelationalLessPrec:
                self.callEqualityExp(escopo)
            else:
                pass

        elif self.lexemToken in self.firstRelationalMorePrec:
            self.getNextToken()
            if self.lexemToken in self.firstAritmeticExp:
                self.callAritmeticExp(escopo)
            else:
                pass
            if self.lexemToken in self.firstRelationalMorePrec:
                self.callInequalityExp(escopo)
            else:
                pass
        else:
            pass


    def callEqualityExp(self, escopo):
        if self.lexemToken in self.firstRelationalLessPrec:
            self.getNextToken()
        else:
            pass
        if self.lexemToken in self.firstAritmeticExp:
            self.callAritmeticExp(escopo)
        else:
            pass
        if self.lexemToken in self.firstRelationalMorePrec:
            self.callInequalityExp(escopo)
        else:
            pass
        if self.lexemToken in self.firstRelationalLessPrec:
            self.callEqualityExp(escopo)
        else:
            pass


    def callInequalityExp(self, escopo):
        if self.lexemToken in self.firstRelationalMorePrec:
            self.getNextToken()
        else:
            pass
        if self.lexemToken in self.firstAritmeticExp:
            self.callAritmeticExp(escopo)
        else:
            pass
        if self.lexemToken in self.firstRelationalLessPrec:
            self.callEqualityExp(escopo)
        else:
            pass


    def callAritmeticExp(self, escopo):
        if self.lexemToken in self.firstOpUnary:
            self.callOperation(escopo)
            if self.lexemToken in self.firstPlusMinus:
                self.callOpSum(escopo)
            else:
                pass
        elif self.lexemToken == '(':
            self.getNextToken()
            if self.lexemToken in self.firstAritmeticExp:
                self.callRelationalExp(escopo)
            else: 
                pass
            if self.lexemToken == ')':
                self.getNextToken()
            else:
                pass
        else:
            pass    


    def callOperation(self, escopo):
        if self.lexemToken in self.firstOpUnary:
            self.callOpUnary(escopo)
        else:
            pass
        if self.lexemToken in self.firstTimesDivision:
            self.callOpMultiplication(escopo)
        else: 
            pass


    def callOpSum(self, escopo):
        if self.lexemToken in self.firstPlusMinus:
            self.getNextToken()
        else:
            pass
        if self.lexemToken in self.firstOpUnary:
            self.callOperation(escopo)
        else:
            pass
        if self.lexemToken in self.firstPlusMinus:
            self.getNextToken()
        else:
            pass  
        

    def callOpMultiplication(self, escopo):
        if self.lexemToken in self.firstTimesDivision:
            self.getNextToken()
        else:
            pass
        if self.lexemToken in self.firstUnaryOP:
            self.callOpUnary(escopo)
        else:
            pass
        if self.lexemToken in self.firstTimesDivision:
            self.callOpMultiplication(escopo) 


    def callOpUnary(self, escopo):
        if self.lexemToken in self.firstUnaryOP:
            self.callUnaryOp(escopo)
        elif self.lexemToken in self.firstFinalValue:
            self.callFinalValue(escopo)
        elif self.lexemToken == '(':
            self.getNextToken()
            if self.lexemToken in self.firstAritmeticExp:
                self.callAritmeticExp(escopo)
            else:
                pass
            if self.lexemToken == ')':
                self.getNextToken()
        else:
            pass


    def callUnaryOp(self, escopo):
        if self.lexemToken in self.firstUnaryOP:
            self.getNextToken()
            if self.lexemToken in self.firstFinalValue:
                self.callFinalValue(escopo)
        elif self.lexemToken in self.firstFinalValue:
            self.callFinalValue(escopo)
            if self.lexemToken in self.firstUnaryOP:
                self.getNextToken()
        elif self.lexemToken == '!':
            if self.lexemToken in self.firstCallVariable:
                real_escopo = ""
                variable = ""
                structs_name = ""
                array_size = []
                line = self.errorLineToken
                real_escopo, variable, structs_name, array_size = self.callCallVariable(escopo, real_escopo, variable, structs_name, array_size)
                self.semantic.check_read_print(real_escopo, variable, structs_name, array_size, line)


    def callFinalValue(self, escopo):
        if self.lexemToken in self.firstCallVariable:
            real_escopo = ""
            variable = ""
            structs_name = ""
            array_size = []
            line = self.errorLineToken
            real_escopo, variable, structs_name, array_size = self.callCallVariable(escopo, real_escopo, variable, structs_name, array_size)
            self.semantic.check_read_print(real_escopo, variable, structs_name, array_size, line)
        elif self.typeLexema == 'NRO':
            self.getNextToken()
        elif self.getNextToken in self.firstBooleanos:
            self.getNextToken()
        else:
            pass


    def callCallVariable(self, escopo, real_escopo, variable, structs_name, array_size):
        if self.lexemToken in self.firstModifier:
            if (self.lexemToken == "local"):
                real_escopo = escopo
            else:
                real_escopo = "global_var"
            self.getNextToken()
        else:
            while (not ((self.lexemToken in self.firstModifier) or (self.lexemToken == ".") or (self.lexemToken in self.FollowCallVariable)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, self.firstModifier))
                self.getNextToken()
            if (not self.lexemToken in self.firstModifier):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "modificador", ""))
            elif (self.lexemToken in self.firstModifier):
                self.getNextToken()

        if self.lexemToken == '.':
            self.getNextToken()
        else:
            while (not ((self.lexemToken == '.') or (self.typeLexema == "IDE") or (self.lexemToken in self.FollowCallVariable)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["."]))
                self.getNextToken()
            if (not self.lexemToken == '.'):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", "."))
            elif (self.lexemToken == '.'):
                self.getNextToken()

        if self.typeLexema == "IDE":
            variable = self.lexemToken
            if variable in self.semantic.table_var['global_const']['ide']:
                real_escopo = "global_const"
            self.getNextToken()
        else:
            while (not ((self.typeLexema == "IDE") or (self.lexemToken in self.firstPaths) or (self.lexemToken in self.FollowCallVariable)) and (not self.lexemToken == None)):
                self.listErrors.append(self.errorMessagePanic(self.errorLineToken, self.typeLexema, self.lexemToken, ["identificador"]))
                self.getNextToken()
            if (not self.typeLexema == "IDE"):
                self.listErrors.append(self.errorMessage(self.errorLineToken, "identificador", ""))
            elif (self.typeLexema == "IDE"):
                self.getNextToken()
        if self.lexemToken in self.firstPaths:
            structs_name, array_size = self.callPaths(escopo, structs_name, array_size)
        
        return real_escopo, variable, structs_name, array_size

    
    def callReturn(self, escopo):
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
        
        real_escopo = ""
        variable = ""
        structs_name = ""
        array_size = []
        line = self.errorLineToken
        real_escopo, variable, structs_name, array_size = self.callCallVariable(escopo, real_escopo, variable, structs_name, array_size)
        
        self.semantic.check_return(real_escopo, variable, line)

        if self.lexemToken == ";":
            self.getNextToken()
        else:
            self.listErrors.append(self.errorMessage(self.errorLineToken, "simbolo", ";"))

        
    def errorMessage(self, lineError, typeError, expectedValue):
        string = ""
        if(typeError == "palavra"):
            string = string + "Erro sintático na linha: " + str(lineError+1) + ". ## " + "Palavra esperada e não encontrada: " + "'" + expectedValue + "'."
        
        elif(typeError == "simbolo"):
            string = string + "Erro sintático na linha: " + str(lineError+1) + ". ## " + "Simbolo esperado e não encontrado: " + "'" + expectedValue + "'."
        
        elif(typeError == "identificador"):
            string = string + "Erro sintático na linha: " + str(lineError+1) + ". ## " + "Tipo 'identitificador[IDE]' esperado e não encontrado."

        elif(typeError == "tipo"):
            string = string + "Erro sintático na linha: " + str(lineError+1) + ". ## " + "Palavra esperada e não encontrada: " +  "'int', 'real', 'boolean' ou 'string'."
        
        elif(typeError == "parametros"):
            if (expectedValue == "R"):
                string = string + "Erro sintático na linha: " + str(lineError+1) + ". ## " + "Palavra esperada e não encontrada: " +  "'local' ou 'global'."    
            elif (expectedValue == "P"):
                string = string + "Erro sintático na linha: " + str(lineError+1) + ". ## " + "Palavra esperada e não encontrada: " +  "[tipo: CADEIA DE CARACTERES], 'local' ou 'global'."

        elif(typeError == "modificador"):
            string = string + "Erro sintático na linha: " + str(lineError+1) + ". ## " + "Palavra esperada e não encontrada: " +  "'local' ou 'global'."

        elif(typeError == "valor"):
            string = string + "Erro sintático na linha: " + str(lineError+1) + ". ## " + "Valor esperado e não encontrado: " +  "[tipo: NUMERO], [tipo: CADEIA DE CARACTERES], 'true' ou 'false'."

        elif(typeError == "NRO_I"):    
            string = string + "Erro sintático na linha: " + str(lineError+1) + ". ## " + "Valor esperado e não encontrado: " +  "[tipo: NUMERO INTEIRO]."

        return string

    
    def errorMessagePanic(self, lineError, typeLexem, valuexem, expectativeCon):
        string = ""

        string = string + "Erro sintático na linha: " + str(lineError+1) + ". ## " + "Palavra/caractere encontrado: " + "'" + valuexem + "'" + "[" + typeLexem + "]" + " ## " + "Palavras/caracteres esperados: "

        for aux in expectativeCon:
            if (aux == "IDE"):
                if aux == expectativeCon[len(expectativeCon) - 1]:
                    string = string + "[tipo: IDENTIFICADOR]"
                else:
                    string = string + "[tipo: IDENTIFICADOR]" + ", "

            elif (aux == "CDC"):
                if aux == expectativeCon[len(expectativeCon) - 1]:
                    string = string + "[tipo: CADEIA DE CARACTERE]"
                else:
                    string = string + "[tipo: CADEIA DE CARACTERE]" + ", "

            elif (aux == "NRO"):
                if aux == expectativeCon[len(expectativeCon) - 1]:
                    string = string + "[tipo: NUMERO]"
                else:
                    string = string + "[tipo: NUMERO]" + ", "
            
            else:
                if aux == expectativeCon[len(expectativeCon) - 1]:
                    string = string + "'" + aux + "'"
                else:
                    string = string + "'" + aux + "'" + ", "

        return string


    def writeFiles(self):
        pass

    def teste(self):
        print(self.listErrors)

    def get_output_list(self):
        return self.listErrors