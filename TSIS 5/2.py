import re
s = input()

def function(s):
        patterns = 'ab*?'
        if re.search(patterns, s):
                return True
        else:
                return False

print(function(s))
