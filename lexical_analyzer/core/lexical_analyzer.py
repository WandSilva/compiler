
import sys
import os.path

import string

class LexicalAnalyzer:
    def __init__(self):
        tokenNumber = 0

    def increaseTokenNumber(self):
        self.tokenNumber = self.tokenNumber + 1

    def classifyToken (self):
        pass
    def separateToken(self):
        pass

'''
def main():
    i1 = "a=1;"
    i2 = "x>1"
    i3 = "x>=1"
    i4 = "x<1"
    i5 = "x<=1"
    i6 = "x!=1"
    i7 = "x = = 1"
    
    input_test = i7 
    print("entrada:" + input_test)  
    output = relational_operators(input_test)
    print(output)

def relational_operators (inputA):
    input_split = list(inputA)
    
    for i in range (0, len(input_split)):
        if(input_split[i] == "="):
            if(input_split[i+1] == '='):
                return "opetator: == "
            else:            
                return"operator: ="
        elif(input_split[i] == ">"):
            if(input_split[i+1] == '='):
                return "opetator: >="
            else:            
                return "operator: >"
        elif(input_split[i] == "<"):
            if(input_split[i+1] == '='):
                return "opetator: <="
            else:            
                return "operator: <"
        elif(input_split[i] == "!"):
            if(input_split[i+1] == '='):
                return "opetator: !="


if __name__ == "__main__":
    main()
'''