import re
s = input()

def function(s):
        formula = '\Bz\B'
        if re.search(formula, s):
            print('Match!')
        else:
            print('No match!')

function(s)