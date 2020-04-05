import re 

class semantic_analyzer:
    
    def __init__(self):
        self.table_var = dict()
        self.table_struct = dict()
        self.table_array = dict()
        self.table_func = dict(key_ide = [], ide = [], tipo = [], type_params = [], params = [], num_params = [])
        self.semantic_errors = []

    #MÉTODOS PARA MANIPULAR A TABELA DE VARIÁVEIS
    def __contains_var(self, scope, ide):
        if scope in self.table_var.keys():
            if ide in self.table_var[scope]['ide']:
                return True
        return False

    def add_var(self, scope, tipo, ide, value, line):
        if self.__contains_var(scope, ide):
            self.__msg_error_var ('VAR_JD', scope, ide, line)
        else:
            if scope not in self.table_var.keys():
                self.__add_var_scope(scope)
            self.table_var[scope]['tipo'].append(tipo)
            self.table_var[scope]['ide'].append(ide)
            self.table_var[scope]['value'].append(value)


    def __add_var_scope(self, scope):
        self.table_var[scope] = dict(tipo = [], ide = [], value = [])

    #método pra atribuir valor
    def assign_var(self, ide, scope1, value, scope2, assign_type, line):
        if not self.__contains_var(scope1, ide): #verifica se a variavel não existe
            self.__msg_error_var ('VAR_ND', scope1, ide, line)
    
        else:
            if(assign_type == 'primitivo'): #se for uma atribuição com valores normais
                if self.__is_corect_type(scope1, ide, value, 'var'): #verifica se o tipo ta certo
                    index = self.table_var[scope1]['ide'].index(ide)
                    self.table_var[scope1]['value'][index] = value #bota na tabela
                else:
                    self.__msg_error_var ('VAR_TI', scope1, ide, line)
                    print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')
        
            elif(assign_type == 'variavel'): 
                self.__assign_var_to_var(scope1, ide, value, scope2)

            elif(assign_type == 'func'): 
                self.__assign_func_to_var(scope1, ide, value)

            elif(assign_type == 'array'):
                self.__assign_array_to_var(scope1, ide, value, scope2)

            elif(assign_type == 'exp'):
                pass

    def __assign_var_to_var(self, scope1, ide, value, scope2, line):
        if not self.__contains_var(scope2, value): #verifica se a variavel não existe
            self.__msg_error_var ('VAR_ND', scope2, value, line)
            #print('FAZER A CHAMADA DO ERRO AQUI: #variável não declarada anteriormente') 
        else:
            index_var1 = self.table_var[scope1]['ide'].index(ide)
            tipo_var1 = self.table_var[scope1]['tipo'][index_var1]

            index_var2 = self.table_var[scope2]['ide'].index(value)
            tipo_var2 = self.table_var[scope2]['tipo'][index_var2]
            value_var2 = self.table_var[scope2]['value'][index_var2]
            
            if(tipo_var1 == tipo_var2):
                self.table_var[scope1]['value'][index_var1] = value_var2 #bota na tabela
            else:
                self.__msg_error_var ('VAR_TI', scope1, ide, line)
                # print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')

    def __assign_array_to_var(self, scope1, ide, value, scope2, line):
        if not self.__contains_array(scope2, value): #verifica se o array não existe
            print('FAZER A CHAMADA DO ERRO AQUI: #array não declarado anteriormente') 
        else:
            index_var = self.table_var[scope1]['ide'].index(ide)
            tipo_var = self.table_var[scope1]['tipo'][index_var]

            index_array = self.table_array[scope2]['ide'].index(value)
            tipo_array = self.table_array[scope2]['tipo'][index_array]
            
            if(tipo_var != tipo_array):
                self.__msg_error_var ('VAR_TI', scope1, ide, line)
                #print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')

    def __assign_func_to_var(self, scope1, ide, value, line):
        if not self.__contains_func_ide(value): #verifica se a função não existe
            print('FAZER A CHAMADA DO ERRO AQUI: #função não declarada') 
        else:
            index_var = self.table_var[scope1]['ide'].index(ide)
            tipo_var = self.table_var[scope1]['tipo'][index_var]

            index_func = self.table_func['ide'].index(value)
            tipo_func = self.table_func['tipo'][index_func]
            
            if(tipo_var == tipo_func):
                self.table_var[scope1]['value'][index_var] = value #verificar oq vai ficar armazenado
            else:
                #print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')
                self.__msg_error_var ('VAR_TI', scope1, ide, line)


    def __is_corect_type(self, scope, ide, value, tipo_busca):
        index = 0
        tipo = ''
        if tipo_busca == 'var':
            index = self.table_var[scope]['ide'].index(ide)
            tipo = self.table_var[scope]['tipo'][index]
        elif tipo_busca == 'array':
            index = self.table_array[scope]['ide'].index(ide)
            tipo = self.table_array[scope]['tipo'][index]

        if tipo == 'int':
            if isinstance(int(value), int):
                return True
            else:
                return False

        if tipo == 'float':
            if re.match(r'^-?\d+(?:\.\d+)$', value) is None:
                return False
            else:
                return True

        if tipo == 'string':
            if (value != 'false' and value != 'true') and not value[0].isdigit():
                return True
            else:
                return False

        if tipo == 'boolean':
            if value == 'false' or value == 'true':
                return True
            else:
                return False
    

    #MÉTODOS PARA MANIPULAR A TABELA DE STRUCTS
    def __contains_struct(self, ide, scope):
        struct_key = ide+'ç'+scope
        return True if struct_key in self.table_struct.keys() else False
       

    def add_struct(self, ide, scope, extend, line, type_atrributes, atrributes, tipo_array, ide_array, size1_array, size2_array, size3_array, lines_arrays):
        struct_key = ide+'ç'+scope
        if struct_key not in self.table_struct:
            self.__add_struct_key(struct_key)

        if self.__contains_struct(ide, scope):
            print('FAZER A CHAMADA DO ERRO AQUI: #sctruct ja declarada')
        else:
            self.table_struct[struct_key]['ide'] = ide
            self.table_struct[struct_key]['scope'] = scope
            self.table_struct[struct_key]['type_atrributes'].append(type_atrributes)
            self.table_struct[struct_key]['atrributes'].append(atrributes)
            self.table_struct[struct_key]['extend'] = extend

    def __add_struct_key(self, strcut_key):
        self.table_struct[strcut_key] = dict(ide = None, scope = None, extend = None, type_atrributes = [], atrributes = [])

    
    #MÉTODOS PARA MANIPULAR A TABELA DE ARRAYS
    def __contains_array(self, scope, ide):
        if scope in self.table_array.keys():
            if ide in self.table_array[scope]['ide']:
                return True
        return False

    def add_array(self, scope, tipo, ide, size1, size2, size3, line):
        if scope not in self.table_array:
            self.__add_array_scope(scope)

        if self.__contains_array(scope, ide):
            print('FAZER A CHAMADA DO ERRO AQUI: #array ja declarado')
            return None

        if (size1[0].isdigit() and size2[0].isdigit() and size1[0].isdigit()):
            if not (isinstance(int(size1), int) and isinstance(int(size2), int) and isinstance(int(size3), int)):
                print('FAZER A CHAMADA DO ERRO AQUI: #array dim deve ser um int')
                return None
        else:
            print('FAZER A CHAMADA DO ERRO AQUI: #array dim deve ser um int')
            return None

        self.table_array[scope]['tipo'].append(tipo)
        self.table_array[scope]['ide'].append(ide)
        self.table_array[scope]['size1'].append(size1)
        self.table_array[scope]['size2'].append(size2)
        self.table_array[scope]['size3'].append(size3)

    def __add_array_scope(self, scope): 
        self.table_array[scope] = dict(tipo = [], ide = [], size1 = [], size2 = [], size3 = [])

    def assign_array(self, ide, scope1, value, scope2, assign_type, line):
        if not self.__contains_array(scope1, ide): #verifica se o array não existe
            print('FAZER A CHAMADA DO ERRO AQUI: #array não declarado anteriormente') 
        else:
            if(assign_type == 'primitivo'): #se for uma atribuição com valores normais
                if not self.__is_corect_type(scope1, ide, value, 'array'): #verifica se o tipo ta certo
                    print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')
        
            elif(assign_type == 'variavel'): 
                self.__assign_var_to_array(ide, scope1, value, scope2)

            elif(assign_type == 'func'): 
                self.__assign_func_to_array(ide, scope1, value)

            elif(assign_type == 'array'):
                self.__assign_array_to_array(ide, scope1, value, scope2)

            elif(assign_type == 'exp'):
                pass

    def __assign_var_to_array(self, ide, scope1, value, scope2):
        if not self.__contains_var(scope2, value): #verifica se a variavel não existe
            print('FAZER A CHAMADA DO ERRO AQUI: #variável não declarada anteriormente') 
        else:
            index_array = self.table_array[scope1]['ide'].index(ide)
            tipo_array = self.table_array[scope1]['tipo'][index_array]

            index_var2 = self.table_var[scope2]['ide'].index(value)
            tipo_var2 = self.table_var[scope2]['tipo'][index_var2]
            
            if(tipo_array != tipo_var2):
                print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')

    def __assign_func_to_array(self, ide, scope1, value):
        if not self.__contains_func_ide(value): #verifica se a função não existe
            print('FAZER A CHAMADA DO ERRO AQUI: #função não declarada') 
        else:
            index_array = self.table_array[scope1]['ide'].index(ide)
            tipo_array = self.table_array[scope1]['tipo'][index_array]

            index_func = self.table_func['ide'].index(value)
            tipo_func = self.table_func['tipo'][index_func]
            
            if not (tipo_array == tipo_func):
                print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')

    def __assign_array_to_array(self, ide, scope1, value, scope2):
        if not self.__contains_array(scope2, value): #verifica se o array não existe
            print('FAZER A CHAMADA DO ERRO AQUI: #array não declarado anteriormente') 
        else:
            index_array1 = self.table_array[scope1]['ide'].index(ide)
            tipo_array1 = self.table_array[scope1]['tipo'][index_array1]

            index_array2 = self.table_array[scope2]['ide'].index(value)
            tipo_array2 = self.table_array[scope2]['tipo'][index_array2]
            
            if(tipo_array1 != tipo_array2):
                print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')

    def check_return (self, scope, ide, line):
        if(not (self.__contains_var(scope, ide))):
            print('FAZER A CHAMADA DO ERRO AQUI: #variavel não declarada no escopo')
        else:
            index_var1 = self.table_var[scope]['ide'].index(ide)
            tipo_var1 = self.table_var[scope]['tipo'][index_var1]

            index_func = self.table_func['ide'].index(scope)
            tipo_func = self.table_func['tipo'][index_func]

            if (not(tipo_var1 == tipo_func)):
                print('FAZER A CHAMADA DO ERRO AQUI: #variável de retorno tem tipo diferente da função ')






    #MÉTODOS PARA MANIPULAR A TABELA DE FUNÇÕES
    def __contains_func_key(self, key_ide):
        return True if key_ide in self.table_func['key_ide'] else False

    def __contains_func_ide(self, ide):
        return True if ide in self.table_func['ide'] else False

    def add_func(self, ide, tipo, type_params, params, line):
        key_ide = ide
        for item in type_params:
            key_ide= key_ide+'_ç_'+item
        if self.__contains_func_key(key_ide):
            print('FAZER A CHAMADA DO ERRO AQUI: #função existente')
        else:
            self.table_func['key_ide'].append(key_ide)
            self.table_func['ide'].append(ide)
            self.table_func['tipo'].append(tipo)
            self.table_func['type_params'].append(type_params)
            self.table_func['params'].append(params)
            self.table_func['num_params'].append(len(params))

    def call_func(self, scope, ide_func, params, type_tokens_params, line):
        type_params = self.__get_params_type(scope, params, type_tokens_params)
        key_ide = ide_func
        for item in type_params:
            key_ide= key_ide+'_ç_'+item

        if not self.__contains_func_key(key_ide):
            print('FAZER A CHAMADA DO ERRO AQUI: #funcao não declarada anteriormente') 


    def __get_params_type(self, scope, params, type_tokens_params):
        params_type = []

        for i in range (0, len(params)):

            if type_tokens_params[i] == 'IDE':
                param = params[i]
                if self.__contains_var(scope, param):
                    index_var = self.table_var[scope]['ide'].index(param)
                    tipo_var = self.table_var[scope]['tipo'][index_var]
                    params_type.append(tipo_var)
                else:
                    print('FAZER A CHAMADA DO ERRO AQUI: #variável não declarada anteriormente') 

            elif type_tokens_params[i] == 'NRO':
                param = params[i]
                if isinstance(int(param), int):
                    params_type.append('int')
                elif re.match(r'^-?\d+(?:\.\d+)$', param) is not None:
                    params_type.append('float')

            elif type_tokens_params[i] == 'CDC':
                params_type.append('string')

            elif type_tokens_params[i] == 'PRE':
                params_type.append('boolean')
        
        return params_type


    #MANIPULAÇÃO DOS ERROS

    def __msg_error_var (self, typeError, scope, ide, lineError):
        if (typeError == "VAR_JD"): #VARIÁVEL JÁ DECLARADA
            error = 'variavel ' + ide + ' ja declarada no escopo '+ scope + '. linha '+lineError
            self.semantic_errors.append(error)
        elif (typeError == "VAR_ND"): #VARIÁVEL NÃO DECLARADA
            error = 'variavel ' + ide + ' nao declarada no escopo '+ scope + '. linha '+lineError
            self.semantic_errors.append(error)
        elif (typeError == "VAR_TI"): #ATRIBUIÇÃO DE VALOR INCOMPATIVEL COM O TIPO
            error = 'atribuição não compativel com o tipo da variavel ' + ide + '. linha '+lineError
            self.semantic_errors.append(error)

    def __msg_error_func(self, typeError, ide, lineError):
        if (typeError == "FUNC_JD"): #FUNC JÁ DECLARADA
            error = 'funcao ' + ide + ' ja declarada. linha '+lineError
            self.semantic_errors.append(error)
        elif (typeError == "FUNC_ND"): #FUNC NÃO DECLARADA
            error = 'funcao ' + ide + ' nao declarada. linha '+lineError
            self.semantic_errors.append(error)
        elif (typeError == "FUNC_RETURN"): #RETORNO INCOMPATÍVEL
            error = 'retorno não compativel com o tipo da funcao ' + ide + '. linha '+lineError
            self.semantic_errors.append(error)

    def __msg_error_struct(self, typeError, scope, ide, lineError):
        if (typeError == "STRUCT_JD"): #STRUCT JÁ DECLARADA
            error = 'struct ' + ide + ' ja declarada no escopo '+ scope + '. linha '+lineError
            self.semantic_errors.append(error)
        elif (typeError == "STRUCT_ND"): #STRUCT NÃO DECLARADA
            error = 'struct ' + ide + ' nao declarada no escopo '+ scope + '. linha '+lineError
            self.semantic_errors.append(error)

    def __msg_semantic_errors_const(self, name, typeConst, valor, typeError):
        pass
    
    def __print_semantic_errors(self):
        print(self.semantic_errors)
    #-------------------------- ARRUMAR ANTES DE ENVIAR -----------------------------------
    #PARA TESTE
    def get_structs(self):
        return self.table_struct
    
    def get_vars(self):
        return self.table_var

    def get_funcs(self):
        return self.table_func

    def get_arrays(self):
        return self.table_array