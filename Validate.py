import inspect
from input_and_tokens import *

def validate(tokens):
    num_count = 0
    flag = True    
    for i in tokens:
        if type(i) == int or i in variables:
            num_count += 1
        elif i in operations:
            if len(inspect.signature(operations[i]).parameters) == 1:
                if num_count < 1:
                    flag = False
                    print("ERROR: Too few arguments given for '" + i + "'")
                    #break
            elif len(inspect.signature(operations[i]).parameters) == 2:
                if num_count < 2:
                    flag = False
                    print("ERROR: Too few arguments given for '" + i + "'")
                    #break
                num_count -= 1
        else:
            print("ERROR: Element '" + str(i) + "' is invalid")
            flag = False
            #break
    if num_count != 1 and flag:
        print("ERROR: Too many numbers given")
        flag = False
    return flag
