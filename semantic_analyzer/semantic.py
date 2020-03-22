class semantic_analyzer:
    
    def __init__(self):
        self.table_var = dict()
        self.table_struct = dict()
        self.table_array = dict()
        self.table_func = dict(ide = [], tipo = [], type_params = [], params = [], num_params = [])

    #MÉTODOS PARA MANIPULAR A TABELA DE VARIÁVEIS
    def contains_var(self, scope, ide):
        return True if ide in self.table_var[scope]['ide'] else False

    def add_var(self, scope, tipo, ide, value):
        if scope not in self.table_var:
            self.__add_var_scope(scope)
        self.table_var[scope]['tipo'].append(tipo)
        self.table_var[scope]['ide'].append(ide)
        self.table_var[scope]['value'].append(value)

    def __add_var_scope(self, scope):
        self.table_var[scope] = dict(tipo = [], ide = [], value = [])


    #MÉTODOS PARA MANIPULAR A TABELA DE STRUCTS
    def contains_struct(self, ide, scope):
        return True if ide in self.table_struct[scope]['ide'] else False

    #POSSIVEL?
    def add_struct(self, scope, ide, variables, extend):
        if scope not in self.table_struct:
            self.__add_struct_scope(scope)
        dict(ide = [], variables = [], extend = [])
        self.table_struct[scope]['ide'].append(ide)
        self.table_struct[scope]['var'].append(variables)
        self.table_struct[scope]['extend'].append(extend)

    def __add_struct_scope(self, scope):
        self.table_struct[scope] = dict(ide = [], variables = [], extend = [])

    #def add_struct(self, scope, ide, type_atrributes, atrributes, extend):
    #    if scope not in self.table_struct:
    #        self.__add_struct_scope(scope)
    #    dict(ide = [], type_atrributes = [], atrributes = [], extend = [])
    #    self.table_struct[scope]['ide'].append(ide)
    #    self.table_struct[scope]['type_atrributes'].append(type_atrributes)
    #    self.table_struct[scope]['atrributes'].append(atrributes)
    #    self.table_struct[scope]['extend'].append(extend)

    #def __add_struct_scope(self, scope):
    #     self.table_struct[scope] = dict(ide = [], type_atrributes = [], atrributes = [], extend = [])

    
    #MÉTODOS PARA MANIPULAR A TABELA DE ARRAYS
    def contains_array(self, var):
        return True

    def add_array(self, var):
        pass


    #MÉTODOS PARA MANIPULAR A TABELA DE FUNÇÕES
    def contains_func(self, ide):
        return True if ide in self.table_func['ide'] else False

    def add_func(self, ide, tipo, type_params, params):
        self.table_func['ide'].append(ide)
        self.table_func['tipo'].append(tipo)
        self.table_func['type_params'].append(type_params)
        self.table_func['params'].append(params)
        self.table_func['num_params'].append(len(params))


    #-------------------------- ARRUMAR ANTES DE ENVIAR -----------------------------------
    #PARA TESTE
    def get_structs(self):
        return self.table_struct
    
    def get_vars(self):
        return self.table_var

    def get_funcs(self):
        return self.table_func