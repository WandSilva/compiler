def main():    
    i1 = "a=1;"
    i2 = "x>1"
    i3 = "x>=1"
    i4 = "x<1"
    i5 = "x<=1"
    i6 = "x!=1"
    
    input_test = i6  
    print("entrada:" + input_test)  
    output = relational_operators(input_test)
    print(output)

def relational_operators (inputA):
    input_split = list(inputA)
    
    for i in range (0, len(input_split)):
        if(input_split[i] == "="):
            if(input_split[i+1] == '='):
                return "opetator: =="
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
