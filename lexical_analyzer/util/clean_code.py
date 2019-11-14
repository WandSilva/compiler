class CleanCode:
    
    def __init__(self):
        pass

    def remove_comments(self, is_block_comment, input_line):
        line = input_line
        
        if(is_block_comment):
            if(line.find("*/") >= 0):
                line = ""
                return [False, line]
            else:
                line = ""
                return[True, line]
            
        elif((line.find("/*") >= 0) and (line.find("*/") >= 0)):
            line=""
            return [False, line]
        elif(line.find("//") >= 0):
            line=""
            return [False, line]
        elif(line.find("/*") >= 0):
            line=""
            return [True, line];
        else:
            return [False, line]