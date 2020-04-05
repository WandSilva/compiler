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
semantic.add_var('start', 'int', 'x', 'None', '1')
semantic.add_var('global', 'int', 'y', '5.1', '2')
semantic.assign_var('z', 'start', '2', 'global', 'primitivo', '3')

#teste add array
#semantic.add_var('start', 'int', 'x', '2')
#semantic.add_array('start', 'int', 'lista', '2', '0', '0')
#semantic.add_array('start', 'float', 'lista2', '2', '0', '0')
#semantic.add_func('add', 'int', ['string', 'boolean'], ['a', 'b'])
#semantic.assign_array('lista', 'start', '2', None,  'primitivo')


#teste add retorno funcao
#semantic.add_var('start', 'int', 'x', '1')
#semantic.add_var('start', 'int', 'y', '2')
semantic.add_func('start', 'int', ['string', 'boolean'], ['a', 'b'], '1')
semantic.add_func('start', 'int', ['string', 'boolean'], ['a', 'b'], '1')
semantic.add_func('add', 'float', ['int', 'int'], ['a', 'b'], '2')
#semantic.assign_var('start', 'x', 'add', 'func')

#semantic.call_func('start', 'add', ['xx', 'false'], ['CDC', 'PRE'])

semantic.check_start()
semantic.print_semantic_errors()

