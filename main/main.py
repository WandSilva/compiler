from lexical_analyzer.core.lexical_analyzer import LexicalAnalyzer
from lexical_analyzer.token.token import Token
from lexical_analyzer.util.clean_code import CleanCode

import os
import glob

tableOfS = []  # Tabela de Simbolos
filesText = []
lexInputCodes = []
auxLexemes = []


def main():
    codes = read_file("../input/")
    cc = CleanCode()
    is_block_comment = False
    newLine = ""
    for code in codes:
        cleanSourceCode = []
        for line in code:
            is_block_comment, newLine = cc.remove_comments(is_block_comment, line)
            cleanSourceCode.append(newLine)
        lexInputCodes.append(cleanSourceCode)
    if is_block_comment:
        print("comentário mal formado")  # arrumar isso aqui depois. Tem que gerar erro
    '''
    lexInputCodes.append("int aloisio = 25;")
    lexInputCodes.append("123.456.789")
    lexInputCodes.append("123. aloisio")
    tableOfS = lex_analyser(lexInputCodes)
    print(tableOfS)
    '''


def lex_analyser(cleanSourceCode):
    la = LexicalAnalyzer(cleanSourceCode)
    tableReturn = la.identify_token()
    return tableReturn


def read_file(path):
    numberFiles = len(glob.glob(path + '*.txt'))
    if numberFiles == 0:
        print ("A pasta de entrada está vazia!")
    codes = []
    for i in range(numberFiles):
        file = path + "entrada" + str(i) + '.txt'
        with open(file) as f:
            codes.append(f.read().splitlines())

    return codes


if __name__ == "__main__":
    main()
