import re
s = input()

def function(s):
        formula = '\w*z.\w*'
        if re.search(formula, s):
            print('Match!')
        else:
            print('No match!')

function(s)
