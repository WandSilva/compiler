#   EXA869 - MI - Processadores de Linguagem de Programação (2019.2)
#   Discentes: Aloisio Junior e Wanderson Silva

#   ARQUIVO PRINCIPAL PARA CHAMADA DOS ANALISADORES

from semantic_analyzer.semantic import semantic_analyzer
import re

semantic = semantic_analyzer()

#teste add primitivo
#semantic.add_var('start', 'int', 'x', None)
#semantic.add_var('start', 'string', 'y', 'cvfr333.5')
#semantic.assign_var('start', 'x', '1', 'primitivo')
#semantic.assign_var('start', 'y', 'novo', 'primitivo')

#teste add variavel
#semantic.add_var('start', 'int', 'x', None)
#semantic.add_var('start', 'float', 'y', '5.1')
#semantic.assign_var('start', 'x', 'y', 'variavel')

#teste add array
semantic.add_var('start', 'int', 'x', '1')
semantic.add_array('start', 'int', 'lista', 'x', '0', '0')
semantic.assign_var('start', 'x', 'lista', 'array')


#teste add retorno funcao
#semantic.add_var('start', 'int', 'x', '1')
#semantic.add_var('start', 'int', 'y', '2')
#semantic.add_func('add', 'int', ['string', 'boolean'], ['a', 'b'])
#semantic.add_func('add', 'float', ['int', 'int'], ['a', 'b'])
#semantic.assign_var('start', 'x', 'add', 'func')

#semantic.call_func('start', 'add', ['xx', 'false'], ['CDC', 'PRE'])


#print(semantic.get_vars())

