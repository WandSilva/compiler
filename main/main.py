from lexical_analyzer.core.lexical_analyzer import LexicalAnalyzer
import glob

all_tokens_list = []  # Tabela de Simbolos
def main():
    lexInputCodes = []
    codes = read_file("../input/")
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
        save_file(tokens_list, comf_list, index+1)
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
        file = path + "entrada" + str(i) + '.txt'
        with open(file) as f:
            codes.append(f.read().splitlines())
    return codes

def save_file(token_list, comf_list, index):
    output_file = "../output/saida"+str(index)
    for token in token_list:
        #open(output_file,'a').write(json.dumps(token.to_dict())+"\n")
        open(output_file,'a').write(token.to_dict()["linha"] + " " +
             token.to_dict()["tipo"] + " " +
             token.to_dict()["lexema"] + "\n")
    
    if(comf_list[index-1] is not None):    
        open(output_file,'a').write("\n\n"+comf_list[index-1]["linha"] + " " +
                 comf_list[index-1]["typeError"] + " " +
                 comf_list[index-1]["lexeme"] + "\n")

if __name__ == "__main__":
    main()

    
    