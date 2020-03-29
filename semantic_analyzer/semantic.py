import re 

class semantic_analyzer:
    
    def __init__(self):
        self.table_var = dict()
        self.table_struct = dict()
        self.table_array = dict()
        self.table_func = dict(ide = [], tipo = [], type_params = [], params = [], num_params = [])
        self.semantic_errors = []

    #MÉTODOS PARA MANIPULAR A TABELA DE VARIÁVEIS
    def __contains_var(self, scope, ide):
        if scope in self.table_var.keys():
            if ide in self.table_var[scope]['ide']:
                return True
        return False

    def add_var(self, scope, tipo, ide, value):
        if self.__contains_var(scope, ide):
            print('FAZER A CHAMADA DO ERRO AQUI: #DECLARANDO UMA JA EXISTENTE') #DECLARANDO UMA JA EXISTENTE
        else:
            if scope not in self.table_var.keys():
                self.__add_var_scope(scope)
            self.table_var[scope]['tipo'].append(tipo)
            self.table_var[scope]['ide'].append(ide)
            self.table_var[scope]['value'].append(value)


    def __add_var_scope(self, scope):
        self.table_var[scope] = dict(tipo = [], ide = [], value = [])

    #método pra atribuir valor
    def assign_var(self, scope, ide, value, assign_type):
        if not self.__contains_var(scope, ide): #verifica se a variavel não existe
            print('FAZER A CHAMADA DO ERRO AQUI: #variável não declarada anteriormente') 
        else:
            if(assign_type == 'primitivo'): #se for uma atribuição com valores normais
                if self.__is_corect_type(scope, ide, value): #verifica se o tipo ta certo
                    index = self.table_var[scope]['ide'].index(ide)
                    self.table_var[scope]['value'][index] = value #bota na tabela
                else:
                    print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')
        
            elif(assign_type == 'variavel'): 
                self.__assign_var_to_var(scope, ide, value)

            elif(assign_type == 'func'): 
                self.__assign_func_to_var(scope, ide, value)

            elif(assign_type == 'exp'):
                pass

    def __assign_var_to_var(self, scope, ide, value):
        if not self.__contains_var(scope, value): #verifica se a variavel não existe
            print('FAZER A CHAMADA DO ERRO AQUI: #variável não declarada anteriormente') 
        else:
            index_var1 = self.table_var[scope]['ide'].index(ide)
            tipo_var1 = self.table_var[scope]['tipo'][index_var1]

            index_var2 = self.table_var[scope]['ide'].index(value)
            tipo_var2 = self.table_var[scope]['tipo'][index_var2]
            value_var2 = self.table_var[scope]['value'][index_var2]
            
            if(tipo_var1 == tipo_var2):
                self.table_var[scope]['value'][index_var1] = value_var2 #bota na tabela
            else:
                print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')

    def __assign_func_to_var(self, scope, ide, value):
        if not self.__contains_func(value): #verifica se a função não existe
            print('FAZER A CHAMADA DO ERRO AQUI: #função não declarada') 
        else:
            index_var = self.table_var[scope]['ide'].index(ide)
            tipo_var = self.table_var[scope]['tipo'][index_var]

            index_func = self.table_func['ide'].index(value)
            tipo_func = self.table_func['tipo'][index_func]
            
            if(tipo_var == tipo_func):
                self.table_var[scope]['value'][index_var] = value #verificar oq vai ficar armazenado
            else:
                print('FAZER A CHAMADA DO ERRO AQUI: #tipo incompatível')


    def __is_corect_type(self, scope, ide, value):
        index = self.table_var[scope]['ide'].index(ide)
        tipo = self.table_var[scope]['tipo'][index]

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
    def contains_struct(self, ide, scope):
        struct_key = ide+'ç'+scope
        return True if struct_key in self.table_struct.keys() else False
       

    def add_struct(self, ide, scope, extend, type_atrributes, atrributes):
        struct_key = ide+'ç'+scope
        if struct_key not in self.table_struct:
            self.__add_struct_key(struct_key)

        self.table_struct[struct_key]['ide'] = ide
        self.table_struct[struct_key]['scope'] = scope
        self.table_struct[struct_key]['type_atrributes'].append(type_atrributes)
        self.table_struct[struct_key]['atrributes'].append(atrributes)
        self.table_struct[struct_key]['extend'] = extend

    def __add_struct_key(self, strcut_key):
        self.table_struct[strcut_key] = dict(ide = None, scope = None, extend = None, type_atrributes = [], atrributes = [])

    
    #MÉTODOS PARA MANIPULAR A TABELA DE ARRAYS
    def contains_array(self, scope, ide):
        if scope in self.table_array.keys():
            if ide in self.table_array[scope]['ide']:
                return True
        return False

    def add_array(self, scope, tipo, ide, size, value):
        if scope not in self.table_array:
            self.__add_array_scope(scope)

        self.table_array[scope]['tipo'].append(tipo)
        self.table_array[scope]['ide'].append(ide)
        self.table_array[scope]['value'].append(value)
        self.table_array[scope]['size'].append(size)

    def __add_array_scope(self, scope): 
        self.table_array[scope] = dict(tipo = [], ide = [], size = [], value = [])


    #MÉTODOS PARA MANIPULAR A TABELA DE FUNÇÕES
    def __contains_func(self, ide):
        return True if ide in self.table_func['ide'] else False

    def add_func(self, ide, tipo, type_params, params):
        self.table_func['ide'].append(ide)
        self.table_func['tipo'].append(tipo)
        self.table_func['type_params'].append(type_params)
        self.table_func['params'].append(params)
        self.table_func['num_params'].append(len(params))

    def var_verification_values(self):
        pass

    def const_verification_values(self):
        pass

    def structs_verification(self):
        pass

    def msg_semantic_errors_var (self, escopo, name, valor, lineError, typeReturnFunction, typeError):
        if (typeError == "VAR_DV"):
            pass
        elif (typeError == "VAR_ND"): #VARIÁVEL NÃO DECLARADA
            pass
        elif (typeError == "VAR_TAVI"): #ATRIBUIÇÃO DE VALOR INCOMPATIVEL COM O TIPO
            pass
        elif (typeError == "VAR_FRI"): #TIPO DE RETORNO DE FUNÇÃO INCOMPATÍVEL COM A VARIAVEL
            pass

    def msg_semantic_errors_const(self, name, typeConst, valor, typeError):
        pass
    
    def print_semantic_errors(self):
        pass
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