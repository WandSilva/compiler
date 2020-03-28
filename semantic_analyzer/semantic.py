class semantic_analyzer:
    
    def __init__(self):
        self.table_var = dict()
        self.table_struct = dict()
        self.table_array = dict()
        self.table_func = dict(ide = [], tipo = [], type_params = [], params = [], num_params = [])
        self.semantic_errors = []

    #MÉTODOS PARA MANIPULAR A TABELA DE VARIÁVEIS
    def contains_var(self, scope, ide):
        if scope in self.table_var.keys():
            if ide in self.table_var[scope]['ide']:
                return True
        return False

    def add_var(self, scope, tipo, ide, value):
        if scope not in self.table_var.keys():
            self.__add_var_scope(scope)
            print("HHHHHHHHHHHHHHHHHHHHHHHHH")

        self.table_var[scope]['tipo'].append(tipo)
        self.table_var[scope]['ide'].append(ide)
        self.table_var[scope]['value'].append(value)

    def __add_var_scope(self, scope):
        self.table_var[scope] = dict(tipo = [], ide = [], value = [])

    def assign_var(self, scope, ide, value):
        index = self.table_var[scope]['ide'].index(ide)
        self.table_var[scope]['value'][index] = value


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
    def contains_func(self, ide):
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