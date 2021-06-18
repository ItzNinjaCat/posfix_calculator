import math
operations = {
    '+' : lambda a, b : b + a,
    '-' : lambda a, b : b - a,
    '*' : lambda a, b : b * a,
    '/' : lambda a, b : b / a,
    'ln' : lambda a : math.log(a),
    'log' : lambda a, b : math.log(b, a)
    }

def input_and_tokenise(tokens):
    str = input("> ")
    str = ' '.join(str.split())
    tokens = str.split(" ")
    for i in range(len(tokens)):
        try:
            tokens[i] = int(tokens[i])
        except:
            pass
    return tokens