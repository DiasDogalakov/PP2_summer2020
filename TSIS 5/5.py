import re
s = input()

def function(s):
    formula = 'ab{3}'
    if re.search(formula, s):
        print('Match!')
    else:
        print('Not match!')

function(s)
