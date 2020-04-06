import re 

class semantic_analyzer:
    
    def __init__(self):
        self.table_var = dict()
        self.table_struct = dict()
        self.table_array = dict()
        self.table_func = dict(key_ide = [], ide = [], tipo = [], type_params = [], params = [], num_params = [])
        self.semantic_errors = []

    ######################   MÉTODOS PARA MANIPULAR A TABELA DE VARIÁVEIS  ################
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

        elif scope1 == 'global_const':
            self.__msg_error_var('VAR_CONST', scope1, ide, line)
    
        else:
            if(assign_type == 'primitivo'): #se for uma atribuição com valores normais
                if self.__is_corect_type(scope1, ide, value, None, 'var'): #verifica se o tipo ta certo
                    index = self.table_var[scope1]['ide'].index(ide)
                    self.table_var[scope1]['value'][index] = value #bota na tabela
                else:
                    #print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')
                    self.__msg_error_var ('VAR_TI', scope1, ide, line)
        
            elif(assign_type == 'variavel'): 
                self.__assign_var_to_var(scope1, ide, value, scope2, line)

            elif(assign_type == 'func'): 
                self.__assign_func_to_var(scope1, ide, value, line)

            elif(assign_type == 'array'):
                self.__assign_array_to_var(scope1, ide, value, scope2, line)

            elif(assign_type == 'exp'):
                pass

            elif(assign_type == 'struct'):
                self.__assign_struct_to_var(scope1, ide ,value, scope2, line)

            else:
                print("TIPO DE ATRIBUIÇÃO INVÁLIDA")

    def __assign_var_to_var(self, scope1, ide, value, scope2, line):
        if not self.__contains_var(scope2, value): #verifica se a variavel não existe
            self.__msg_error_var('VAR_ND', scope2, value, line)
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
            #print('FAZER A CHAMADA DO ERRO AQUI: #função não declarada') 
             self.__msg_error_func('FUNC_ND', value, line)
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

    def __assign_struct_to_var(self, scope1, ide, value, scope2, line):
        if not self.__contains_struct(value[0], scope2):
            self.__msg_error_struct('STRUCT_ND', scope2, value[0], None, line)
        elif not self.__contains_struct_attribute(value[0], scope2, value[1]):
            self.__msg_error_struct('STRUCT_ATT_ND', scope2, value[0], value[1], line)

        else:
            index_var = self.table_var[scope1]['ide'].index(ide)
            tipo_var = self.table_var[scope1]['tipo'][index_var]

            key = value[0] + 'ç' + scope1
            index_att = self.table_struct[key]['attributes'][0].index(value[1])
            tipo_attribute = self.table_struct[key]['type_attributes'][0][index_att]
            
            if(tipo_var == tipo_attribute):
                self.table_var[scope1]['value'][index_var] = value #verificar oq vai ficar armazenado
            else:
                #print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')
                self.__msg_error_var ('VAR_TI', scope1, ide, line)


    def __is_corect_type(self, scope, ide, value, att_if_struct, tipo_busca):
        index = 0
        tipo = ''
        if tipo_busca == 'var':
            index = self.table_var[scope]['ide'].index(ide)
            tipo = self.table_var[scope]['tipo'][index]
        elif tipo_busca == 'array':
            index = self.table_array[scope]['ide'].index(ide)
            tipo = self.table_array[scope]['tipo'][index]
        elif tipo_busca == 'struct':
            key = ide+'ç'+scope
            index = self.table_struct[key]['attributes'][0].index(att_if_struct)
            tipo = self.table_struct[key]['type_attributes'][0][index]

        if tipo == 'int':
            try:
                int(value)
                return True
            except:
                return False

        if tipo == 'real':
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
    

    ##################   MÉTODOS PARA MANIPULAR A TABELA DE STRUCTS ######################
    def __contains_struct(self, ide, scope):
        struct_key = ide+'ç'+scope
        return True if struct_key in self.table_struct.keys() else False

    def __contains_struct_attribute(self, ide, scope, attribute):
        struct_key = ide+'ç'+scope
        return True if attribute in self.table_struct[struct_key]['attributes'][0] else False

    def check_struct_extend(self, scope, ide, extend, line):
        struct_key1 = ide+'ç'+scope
        struct_key2 = extend+'ç'+scope
        if not self.__contains_struct(extend, scope):
            self.__msg_error_struct('STRUCT_ND', scope, extend, None, line)
        else:
            atributos1 = self.table_struct[struct_key1]['attributes'][0]
            atributos2 = self.table_struct[struct_key2]['attributes'][0]
            for item in atributos1:
                if item in atributos2:
                    self.__msg_error_struct('STRCUT_EXTEND', None, None, item, line)
       

    def add_struct(self, ide, scope, type_attributes, attributes, extend, line):
        struct_key = ide+'ç'+scope

        if self.__contains_struct(ide, scope):
            #print('FAZER A CHAMADA DO ERRO AQUI: #sctruct ja declarada')
            self.__msg_error_struct('STRUCT_JD', scope, ide, None, line)

        elif struct_key not in self.table_struct.keys():
            self.__add_struct_key(struct_key)

            self.table_struct[struct_key]['ide'] = ide
            self.table_struct[struct_key]['scope'] = scope
            self.table_struct[struct_key]['type_attributes'].append(type_attributes)
            self.table_struct[struct_key]['attributes'].append(attributes)
            self.table_struct[struct_key]['extend'] = extend
            if extend is not None:
                self.check_struct_extend(scope, ide, extend, line)

    def __add_struct_key(self, strcut_key):
        self.table_struct[strcut_key] = dict(ide = None, scope = None, extend = None, type_attributes = [], attributes = [])

    def assign_struct(self, struct, scope1, value, scope2, assign_type, line):
        if not self.__contains_struct(struct[0], scope1): #verifica se a variavel não existe
            self.__msg_error_struct('STRUCT_ND', scope1, struct[0], struct[1], line)
    
        else:
            if(assign_type == 'primitivo'): #se for uma atribuição com valores normais
                if not self.__is_corect_type(scope1, struct[0], value, struct[1], 'struct'): #verifica se o tipo ta certo
                    self.__msg_error_struct('STRUCT_ATT_TI', scope1, struct[0], struct[1], line)
        
            elif(assign_type == 'variavel'): 
                self.__assign_var_to_struct(struct, scope1, value, scope2, line)

            elif(assign_type == 'func'): 
                self.__assign_func_to_struct(struct, scope1, value, line)

            elif(assign_type == 'array'):
                self.__assign_array_to_struct(struct, scope1, value, scope2, line)

            elif(assign_type == 'exp'):
                pass
            
            elif(assign_type == 'struct'):
                self.__assign_struct_to_struct(scope1, struct, value, scope2, line)


    def __assign_var_to_struct(self, struct, scope1, value, scope2, line):
        if not self.__contains_var(scope2, value): #verifica se a variavel não existe
            #print('FAZER A CHAMADA DO ERRO AQUI: #variável não declarada anteriormente') 
            self.__msg_error_var ('VAR_ND', scope2, value, line)

        else:
            key = struct[0] + 'ç' + scope1
            index_att = self.table_struct[key]['attributes'][0].index(struct[1])
            tipo_attribute = self.table_struct[key]['type_attributes'][0][index_att]

            index_var2 = self.table_var[scope2]['ide'].index(value)
            tipo_var2 = self.table_var[scope2]['tipo'][index_var2]
            
            if(tipo_attribute != tipo_var2):
                #print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')
                self.__msg_error_struct('STRCUT_ATT_TI', scope1, struct[0], struct[1], line)

    def __assign_func_to_struct(self, struct, scope1, value, line):
        if not self.__contains_func_ide(value): #verifica se a função não existe
            #print('FAZER A CHAMADA DO ERRO AQUI: #função não declarada') 
            self.__msg_error_func('FUNC_ND', value, line)
        else:
            key = struct[0] + 'ç' + scope1
            index_att = self.table_struct[key]['attributes'][0].index(struct[1])
            tipo_attribute = self.table_struct[key]['type_attributes'][0][index_att]

            index_func = self.table_func['ide'].index(value)
            tipo_func = self.table_func['tipo'][index_func]
            
            if not (tipo_attribute == tipo_func):
                #print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')
                self.__msg_error_struct('STRCUT_ATT_TI', scope1, struct[0], struct[1], line)

    def __assign_array_to_struct(self, struct, scope1, value, scope2, line):
        if not self.__contains_array(scope2, value): #verifica se o array não existe
            #print('FAZER A CHAMADA DO ERRO AQUI: #array não declarado anteriormente') 
            self.__msg_error_array('ARRAY_ND', scope2, value, line)
        else:
            key = struct[0] + 'ç' + scope1
            index_att = self.table_struct[key]['attributes'][0].index(struct[1])
            tipo_attribute = self.table_struct[key]['type_attributes'][0][index_att]

            index_array2 = self.table_array[scope2]['ide'].index(value)
            tipo_array2 = self.table_array[scope2]['tipo'][index_array2]
            
            if(tipo_attribute != tipo_array2):
                #print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')
                self.__msg_error_struct('STRCUT_ATT_TI', scope1, struct[0], struct[1], line)

    def __assign_struct_to_struct(self, struct, scope1, value, scope2, line):
        if not self.__contains_struct(value[0], scope2):
            self.__msg_error_struct('STRUCT_ND', scope2, value[0], None, line)
        elif not self.__contains_struct_attribute(value[0], scope2, value[1]):
            print(value)
            print("teste 3")
            self.__msg_error_struct('STRUCT_ATT_ND', scope2, value[0], value[1], line)

        key1 = struct[0] + 'ç' + scope1
        index_att1 = self.table_struct[key1]['attributes'][0].index(struct[1])
        tipo_attribute1 = self.table_struct[key1]['type_attributes'][0][index_att1]
        
        key2 = value[0] + 'ç' + scope2
        index_att2 = self.table_struct[key2]['attributes'][0].index(value[1])
        tipo_attribute2 = self.table_struct[key2]['type_attributes'][0][index_att2]

        if(tipo_attribute1 != tipo_attribute2):
            #print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')
            self.__msg_error_struct('STRCUT_ATT_TI', scope1, struct[0], struct[1], line)




    
    #########################   MÉTODOS PARA MANIPULAR A TABELA DE ARRAYS    ##################
    def __contains_array(self, scope, ide):
        if scope in self.table_array.keys():
            if ide in self.table_array[scope]['ide']:
                return True
        return False

    def add_array(self, scope, tipo, ide, size1, size2, size3, line):
        if scope not in self.table_array:
            self.__add_array_scope(scope, line)

        if self.__contains_array(scope, ide):
            #print('FAZER A CHAMADA DO ERRO AQUI: #array ja declarado')
            self.__msg_error_array('ARRAY_JD', scope, ide, line)
            return None

        if (size1[0].isdigit() and size2[0].isdigit() and size3[0].isdigit()):
            if not (isinstance(int(size1), int) and isinstance(int(size2), int) and isinstance(int(size3), int)):
                #   print('FAZER A CHAMADA DO ERRO AQUI: #array dim deve ser um int')
                self.__msg_error_array('ARRAY_DIM', scope, ide, line)
                return None
        else:
            self.__msg_error_array('ARRAY_DIM', scope, ide, line)
            return None

        self.table_array[scope]['tipo'].append(tipo)
        self.table_array[scope]['ide'].append(ide)
        self.table_array[scope]['size1'].append(size1)
        self.table_array[scope]['size2'].append(size2)
        self.table_array[scope]['size3'].append(size3)

    def __add_array_scope(self, scope, line): 
        self.table_array[scope] = dict(tipo = [], ide = [], size1 = [], size2 = [], size3 = [])

    def assign_array(self, ide, scope1, value, scope2, assign_type, line):
        if not self.__contains_array(scope1, ide): #verifica se o array não existe
            self.__msg_error_array('ARRAY_ND', scope1, ide, line)
        else:
            if(assign_type == 'primitivo'): #se for uma atribuição com valores normais
                if not self.__is_corect_type(scope1, ide, value, None, 'array'): #verifica se o tipo ta certo
                    self.__msg_error_array('ARRAY_TI', scope1, ide, line)
        
            elif(assign_type == 'variavel'): 
                self.__assign_var_to_array(ide, scope1, value, scope2, line)

            elif(assign_type == 'func'): 
                self.__assign_func_to_array(ide, scope1, value, line)

            elif(assign_type == 'array'):
                self.__assign_array_to_array(ide, scope1, value, scope2, line)

            elif(assign_type == 'exp'):
                pass

            elif(assign_type == 'struct'):
                self.__assign_struct_to_array(ide, scope1, value, scope2, line)

    def __assign_var_to_array(self, ide, scope1, value, scope2, line):
        if not self.__contains_var(scope2, value): #verifica se a variavel não existe
            #print('FAZER A CHAMADA DO ERRO AQUI: #variável não declarada anteriormente') 
            self.__msg_error_var ('VAR_ND', scope2, value, line)

        else:
            index_array = self.table_array[scope1]['ide'].index(ide)
            tipo_array = self.table_array[scope1]['tipo'][index_array]

            index_var2 = self.table_var[scope2]['ide'].index(value)
            tipo_var2 = self.table_var[scope2]['tipo'][index_var2]
            
            if(tipo_array != tipo_var2):
                #print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')
                self.__msg_error_array('ARRAY_TI', scope1, ide, line)

    def __assign_func_to_array(self, ide, scope1, value, line):
        if not self.__contains_func_ide(value): #verifica se a função não existe
            #print('FAZER A CHAMADA DO ERRO AQUI: #função não declarada') 
            self.__msg_error_func('FUNC_ND', value, line)
        else:
            index_array = self.table_array[scope1]['ide'].index(ide)
            tipo_array = self.table_array[scope1]['tipo'][index_array]

            index_func = self.table_func['ide'].index(value)
            tipo_func = self.table_func['tipo'][index_func]
            
            if not (tipo_array == tipo_func):
                #print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')
                self.__msg_error_array('ARRAY_TI', scope1, ide, line)

    def __assign_array_to_array(self, ide, scope1, value, scope2, line):
        if not self.__contains_array(scope2, value): #verifica se o array não existe
            #print('FAZER A CHAMADA DO ERRO AQUI: #array não declarado anteriormente') 
            self.__msg_error_array('ARRAY_ND', scope2, value, line)
        else:
            index_array1 = self.table_array[scope1]['ide'].index(ide)
            tipo_array1 = self.table_array[scope1]['tipo'][index_array1]

            index_array2 = self.table_array[scope2]['ide'].index(value)
            tipo_array2 = self.table_array[scope2]['tipo'][index_array2]
            
            if(tipo_array1 != tipo_array2):
                #print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')
                self.__msg_error_array('ARRAY_TI', scope1, ide, line)
    
    def __assign_struct_to_array(self, ide, scope1, value, scope2, line):
        if not self.__contains_struct(value[0], scope2):
            self.__msg_error_struct('STRUCT_ND', scope2, value[0], None, line)
        elif not self.__contains_struct_attribute(value[0], scope2, value[1]):
            self.__msg_error_struct('STRUCT_ATT_ND', scope2, value[0], value[1], line)

        index_array = self.table_array[scope1]['ide'].index(ide)
        tipo_array = self.table_array[scope1]['tipo'][index_array]

        key = value[0] + 'ç' + scope1
        index_att = self.table_struct[key]['attributes'][0].index(value[1])
        tipo_attribute = self.table_struct[key]['type_attributes'][0][index_att]

        if(tipo_array != tipo_attribute):
            #print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')
            self.__msg_error_array('ARRAY_TI', scope1, ide, line)
 


    def check_return (self, scope, ide, line):
        if(not (self.__contains_var(scope, ide))):
            #print('FAZER A CHAMADA DO ERRO AQUI: #variavel não declarada no escopo')
            self.__msg_error_var ('VAR_ND', scope, ide, line)

        else:
            index_var1 = self.table_var[scope]['ide'].index(ide)
            tipo_var1 = self.table_var[scope]['tipo'][index_var1]

            index_func = self.table_func['ide'].index(scope)
            tipo_func = self.table_func['tipo'][index_func]

            if (not(tipo_var1 == tipo_func)):
                #print('FAZER A CHAMADA DO ERRO AQUI: #variável de retorno tem tipo diferente da função ')
                self.__msg_error_func('FUNCT_RETURN', '', line)


    ######################     MÉTODOS PARA MANIPULAR A TABELA DE FUNÇÕES     ########################
    def __contains_func_key(self, key_ide):
        return True if key_ide in self.table_func['key_ide'] else False

    def __contains_func_ide(self, ide):
        return True if ide in self.table_func['ide'] else False

    def check_start(self):
        if 'start' not in self.table_func['ide']:
            self.__msg_error_func('FUNC_START_2', None, None)



    def add_func(self, ide, tipo, type_params, params, line):
        if ide == 'start':
            if 'start' in self.table_func['ide']:
                self.__msg_error_func('FUNC_START', ide, line)
                return None

        key_ide = ide
        for item in type_params:
            key_ide= key_ide+'_ç_'+item
        if self.__contains_func_key(key_ide):
            #print('FAZER A CHAMADA DO ERRO AQUI: #função existente')
            self.__msg_error_func('FUNC_JD', ide, line)
        else:
            self.table_func['key_ide'].append(key_ide)
            self.table_func['ide'].append(ide)
            self.table_func['tipo'].append(tipo)
            self.table_func['type_params'].append(type_params)
            self.table_func['params'].append(params)
            self.table_func['num_params'].append(len(params))

    def call_func(self, scope, ide_func, params, type_tokens_params, line):
        type_params = self.__get_params_type(scope, params, type_tokens_params, line)
        key_ide = ide_func
        for item in type_params:
            key_ide= key_ide+'_ç_'+item

        if not self.__contains_func_key(key_ide):
            #print('FAZER A CHAMADA DO ERRO AQUI: #funcao não declarada anteriormente') 
            self.__msg_error_func('FUNC_ND', ide_func, line)


    def __get_params_type(self, scope, params, type_tokens_params, line):
        params_type = []

        for i in range (0, len(params)):

            if type_tokens_params[i] == 'IDE':
                param = params[i]
                if self.__contains_var(scope, param):
                    index_var = self.table_var[scope]['ide'].index(param)
                    tipo_var = self.table_var[scope]['tipo'][index_var]
                    params_type.append(tipo_var)
                else:
                    #print('FAZER A CHAMADA DO ERRO AQUI: #variável não declarada anteriormente') 
                    self.__msg_error_var('VAR_ND', scope, params, line)

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
        lineError = int(lineError) + 1
        if (typeError == "VAR_JD"): #VARIÁVEL JÁ DECLARADA
            error = 'Variável ' + "'" + str(ide) + "'" + ' ja declarada no escopo '+ "'" + scope + "'" + '. linha '+ str(lineError)
            self.semantic_errors.append(error)
        elif (typeError == "VAR_ND"): #VARIÁVEL NÃO DECLARADA
            error = 'Variável ' + "'" + str(ide) + "'" + ' nao declarada no escopo '+ "'" + scope + "'" + '. linha '+ str(lineError)
            self.semantic_errors.append(error)
        elif (typeError == "VAR_TI"): #ATRIBUIÇÃO DE VALOR INCOMPATIVEL COM O TIPO
            error = 'Atribuição não compativel com o tipo da variavel ' + "'" + ide + "'" + '. linha '+ str(lineError)
            self.semantic_errors.append(error)

    def __msg_error_func(self, typeError, ide, lineError):
        lineError = int(lineError) + 1
        if (typeError == "FUNC_JD"): #FUNC JÁ DECLARADA
            error = 'Função ' + "'" + ide + "'" + ' já declarada. linha '+ str(lineError)
            self.semantic_errors.append(error)
        elif (typeError == "FUNC_ND"): #FUNC NÃO DECLARADA
            error = 'Função ' + "'" + ide + "'" + ' não declarada. linha '+ str(lineError)
            self.semantic_errors.append(error)
        elif (typeError == "FUNC_RETURN"): #RETORNO INCOMPATÍVEL
            error = 'Retorno não compatível com o tipo da função ' + "'" + ide + "'" + '. linha '+ str(lineError)
            self.semantic_errors.append(error)
        elif (typeError == "FUNC_START"): 
            error = 'o programa já contem um procedimento start. linha '+ str(lineError)
            self.semantic_errors.append(error)
        elif (typeError == "FUNC_START_2"): 
            error = "O programa não contem um procedimento 'start'."
            self.semantic_errors.append(error)

    def __msg_error_struct(self, typeError, scope, ide, attribute, lineError):
        lineError = int(lineError) + 1
        if (typeError == "STRUCT_JD"): #STRUCT JÁ DECLARADA
            error = 'Struct ' + "'" + ide + "'" + ' já declarada no escopo ' + "'" + scope + "'" + '. Linha '+ str(lineError)
            self.semantic_errors.append(error)
        elif (typeError == "STRUCT_ND"): #STRUCT NÃO DECLARADA
            error = 'Struct ' + "'" + ide + "'" + ' não declarada no escopo ' + "'" + scope + "'" + '. Linha '+ str(lineError)
            self.semantic_errors.append(error)
        elif (typeError == "STRUCT_ATT_ND"): #STRUCT ATT NÃO DECLARADO
            error = 'Atributo ' + "'" + attribute + "'" + ' da struct ' + "'" + ide + "'" + ' não foi declarado. Linha '+ str(lineError)
            self.semantic_errors.append(error)

        elif (typeError == "STRUCT_ATT_JD"): #STRUCT ATT JÁ DECLARADO
            error = 'Atributo ' + "'" + attribute + "'" + ' da struct ' + "'" + ide + "'" + ' já foi declarado. Linha '+ str(lineError)
            self.semantic_errors.append(error)

        elif (typeError == "STRCUT_ATT_TI"): #ATRIBUIÇÃO DE VALOR INCOMPATIVEL COM O TIPO
            error = 'Atribuição não compativel com o tipo de ' + "'" + ide + '.' + attribute + "'" + '. Linha '+ str(lineError)
            self.semantic_errors.append(error)
        elif (typeError == "STRCUT_EXTEND"): #ATRIBUIÇÃO DE VALOR INCOMPATIVEL COM O TIPO
            error = 'Extend inválido. Atributo ' + "'" + attribute + "'" + ' existente em ambas as structs. Linha '+ str(lineError)
            self.semantic_errors.append(error)


    def __msg_error_array(self, typeError, scope, ide, lineError):
        lineError = int(lineError) + 1
        if (typeError == "ARRAY_JD"): #ARRAY JÁ DECLARADO
            error = 'Array ' + "'" + ide + "'" + ' já declarado no escopo '+ "'" + scope + "'" + '. linha '+ str(lineError)
            self.semantic_errors.append(error)
        elif (typeError == "ARRAY_ND"): #ARRAY NÃO DECLARADA
            error = 'Array ' + "'" + ide + "'" + ' não declarado no escopo '+ "'" + scope + "'" + '. linha '+ str(lineError)
            self.semantic_errors.append(error)
        elif (typeError == "ARRAY_TI"): #ATRIBUIÇÃO DE VALOR INCOMPATIVEL COM O TIPO
            error = 'Atribuição não compativel com o tipo da array ' + "'" + ide + "'" + '. linha '+ str(lineError)
            self.semantic_errors.append(error)
        elif (typeError == "ARRAY_DIM"): #var inválida pra acesso ao array
            error = 'A variável de acesso a posicao do array deve ser um inteiro. linha '+ str(lineError)
            self.semantic_errors.append(error)
    
    def print_semantic_errors(self):
        i = 0
        while (i < len(self.semantic_errors)):
            print(self.semantic_errors[i])
            i = i + 1

    def check_read_print(self, scope, variable, structs_name, array_size, line): # Caso seja uma variavel de uma struct, variable é o nome da struct e structs_name o nome da variavel / array_size é uma lista com os tamanhos do array
        if structs_name == '' and len(array_size) == 0:
            if not self.__contains_var(scope, variable):
                self.__msg_error_var('VAR_ND',scope, variable, line)
        
        elif len(array_size) > 0:
            if not self.__contains_array(scope, variable):
                self.__msg_error_var('ARRAY_ND',scope, variable, line)
        elif structs_name != '':
            if not self.__contains_struct(scope, variable):
                self.__msg_error_struct('STRUCT_ND', scope, variable, structs_name, line)
            elif not self.__contains_struct_attribute(variable, scope, structs_name):
                self.__msg_error_struct('STRUCT_ATT_ND', scope, variable, structs_name, line)


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