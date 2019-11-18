#   EXA869 - MI - Processadores de Linguagem de Programação (2019.2)
#   Discentes: Aloisio Junior e Wanderson Silva

#   ARQUIVO PRINCIPAL PARA CHAMADA DOS ANALISADORES

from lexical_analyzer.core.lexical_analyzer import LexicalAnalyzer
import glob
import os

all_tokens_list = []  # Tabela de Simbolos
input_path = "../input/"
output_path = "../output/"

def main():
    clear_output(output_path)
    lexInputCodes = []
    codes = read_file(input_path)
    la = LexicalAnalyzer()
    comf_list = []
    
    for code in codes:
        cleanCode, comf = la.rmv_comments(code)
        #print(comf)
        comf_list.append(comf)
        lexInputCodes.append(cleanCode)   
         
    for code in lexInputCodes:
        all_tokens_list.append(lex_analyser(code))  
    
    for index, tokens_list in enumerate(all_tokens_list):
        save_file(output_path,tokens_list, comf_list, index+1)
        #for j in tokens_list:
        #    print(j.to_dict())
        
        
def lex_analyser(cleanSourceCode):
    la = LexicalAnalyzer()
    classe = la.identify_token(cleanSourceCode)
    return classe


def read_file(path):
    numberFiles = len(glob.glob(path + '*.txt'))
    if numberFiles == 0:
        print(path)
        print ("A pasta de entrada está vazia!")
    codes = []
    for i in range(numberFiles):
        file = path + "entrada" + str(i+1) + '.txt'
        with open(file) as f:
            codes.append(f.read().splitlines())
    return codes

def save_file(path, token_list, comf_list, index):
    output_file = path+"saida"+str(index)+".txt"
    error_list = []
    for token in token_list:
        if(token.to_dict()["typeError"] == None):
            open(output_file,'a').write(token.to_dict()["linha"] + " " +
                 token.to_dict()["tipo"] + " " +
                 token.to_dict()["lexema"] + "\n")
        else:
            error_list.append(token)  
        
    open(output_file,'a').write("\n\n")      
    for token in error_list:
        open(output_file,'a').write(token.to_dict()["linha"] + " " +
                 token.to_dict()["tipo"] + " " +
                 token.to_dict()["lexema"] + "\n")         
    if(comf_list[index-1] is not None):    
        open(output_file,'a').write(comf_list[index-1]["linha"] + " " +
                 comf_list[index-1]["typeError"] + " " +
                 comf_list[index-1]["lexeme"] + "\n")
        
def clear_output(path):
    direc = os.listdir(path)
    for file in direc:   
        if os.path.exists(path+file):
            os.remove(path+file)


if __name__ == "__main__":
    main()

    
    