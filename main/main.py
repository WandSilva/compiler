from lexical_analyzer.core.lexical_analyzer import LexicalAnalyzer
from lexical_analyzer.token.token import Token    
from lexical_analyzer.util.clean_code import CleanCode

import os
import sys
import glob

tableSimbols = []   # Tabela de Simbolos
filesText = []
cleanSourceCode = []
auxLexemes = []


def main():
    code = read_file("../input/eu.txt");
    cc = CleanCode()
    is_block_comment = False
    newLine = ""
    for line in code:
        is_block_comment, newLine = cc.remove_comments(is_block_comment, line);
        cleanSourceCode.append(newLine)
    if(is_block_comment):
        print("comentário mal formado") #arrumar isso aqui depois. Tem que gerar erro
    
    tableSimbols = lex_analyser(cleanSourceCode)
    print(tableSimbols)
        


def lex_analyser(cleanSourceCode):
    la = LexicalAnalyzer(cleanSourceCode)
    classe = la.identifyToken()
    return classe
    

def read_file(path):
    with open(path) as f:
        lines = f.read().splitlines()      
    return lines

def readFilesAndUpdateFilesTextAux():
    numberFiles = len(glob.glob('../input/*.txt'))

    if (numberFiles == 0):
        print ("A pasta de entrada está vazia!")

    else:
        i = 0
        for i in range(0, numberFiles):
            auxFile = os.path.isfile('../input/entrada' + str(i) + '.txt')  # Se o arquivo existir na pasta, prossegue
            if auxFile:
                fileText = []
                fileAux = open('../input/entrada' + str(i) + '.txt', "r")  # Abre o arquivo de texto específico
                lineText = fileAux.readline()  # Tenta ler uma linha do arquivo de texto
                while lineText is not None:  # Enquanto encontrar uma linha no arquivo de texto, consome o mesmo e
                    # coloca na lista de linhas da lista de arquivo de textos
                    fileText.append(lineText)
                    lineText = fileAux.readline()
                filesText.append(fileText)  # Adiciona a lista de linhas na lista de arquivos de texto
        if len(filesText) == 0:
            print ("Não foi encontrado nenhum arquivo de texto com o formato necessário (entradaX.txt)")


if __name__ == "__main__":
    main()
