import re
s = input()

def function(s):
    formula = '^[a-z]+_[a-z]+$'
    if re.search(formula, s):
        print('Match!')
    else:
         print('No match')

function(s)
