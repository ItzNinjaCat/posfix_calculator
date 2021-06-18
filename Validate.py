def validate(tokens):
    num_count = 0
    flag = True    
    for i in tokens:
        if type(i) == int or i in variables:
            num_count += 1
        '''else:
            print("ERROR: Element '" + str(i) + "' is invalid")
            flag = False'''
            
    return flag
