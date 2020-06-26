import re
s = input()

def function(s):
        formula = '^[a-z]+_[a-z]+$'
        if not re.search(formula, s):
            print('Match!')
        else:
            print('No match!')

function(s)
