import re
s = input()

def function(s):
        formula = '^[a-zA-Z0-9_]*$'
        if re.search(formula, s):
            print('Match!')
        else:
            print('No match!')

function(s)
