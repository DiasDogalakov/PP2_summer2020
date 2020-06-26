import re
s = input()

def function(s):
    formula = 'ab?'
    if re.search(formula, s):
        return 'Match!'
    else:
        return 'Not match!'

print(function(s))
