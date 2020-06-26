import re
s = input()

def function(s):
    formula = re.compile(r".*[0-9]$")
    if formula.match(s):
        print('Match!')
    else:
        print('No match!')

function(s)
