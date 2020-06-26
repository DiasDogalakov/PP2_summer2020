import re
s = input()

def function(s):
        formula = 'ab+?'
        if re.search(formula, s):
                return 'Match!'
        else:
                return('No match!')

print(function(s))
