class semantic_analyzer:
    
    def __init__(self):
        self.table_var = dict()
        self.table_struct = dict()
        self.table_array = dict()
        self.table_func = dict()

    #MÉTODOS PARA MANIPULAR A TABELA DE VARIÁVEIS
    def contains_var(self, scope, ide):
        if ide in self.table_var[scope]['ide']:
            return True
        else:
            return False

    def add_var(self, scope, tipo, ide, value):
        self.table_var[scope]['tipo'].append(tipo)
        self.table_var[scope]['ide'].append(ide)
        self.table_var[scope]['value'].append(value)

    def add_var_scope(self, scope):
        self.table_var[scope] = dict(tipo = [], ide = [], value = [])


    #MÉTODOS PARA MANIPULAR A TABELA DE STRUCTS
    def contains_struct(self, var):
        return True

    def add_struct(self, var):
        pass

    
    #MÉTODOS PARA MANIPULAR A TABELA DE ARRAYS
    def contains_array(self, var):
        return True

    def add_array(self, var):
        pass


    #MÉTODOS PARA MANIPULAR A TABELA DE FUNÇÕES
    def contains_func(self, var):
        return True

    def add_func(self, var):
        pass