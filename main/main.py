from lexical_analyzer.core.lexical_analyzer import LexicalAnalyzer

import glob

tableOfS = []  # Tabela de Simbolos


auxLexemes = []


def main():
    codes = read_file("../input/")
    la = LexicalAnalyzer(cleanSourceCode)
    for code in codes:
        
   
   
    for code in lexInputCodes:
        tableOfS.append(lex_analyser(code))  
    
    for i in tableOfS:
        for j in i:
            print(j.to_dict())

def lex_analyser(cleanSourceCode):
    pass
    la = LexicalAnalyzer(cleanSourceCode)
    classe = la.identify_token()
    return classe


def read_file(path):
    numberFiles = len(glob.glob(path + '*.txt'))
    if numberFiles == 0:
        print(path)
        print ("A pasta de entrada está vazia!")
    codes = []
    for i in range(numberFiles):
        file = path + "entrada" + str(i) + '.txt'
        with open(file) as f:
            codes.append(f.read().splitlines())

    return codes


if __name__ == "__main__":
    main()
