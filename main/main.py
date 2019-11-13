from lexical_analyzer.core.lexical_analyzer import LexicalAnalyzer    # Não consegui ainda resolver esse tipo de importação
from lexical_analyzer.token.token import Token    # Não consegui ainda resolver esse tipo de importação

import os
import sys
import glob

tableSimbols = []  # Tabela de Simbolos
filesText = []


def main():
    # lexicalAnalyzer = LexicalAnalyzer()

    readFilesAndUpdateFilesTextAux()
    # lexicalAnalyzer.startLexicalAnalyzer()


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
