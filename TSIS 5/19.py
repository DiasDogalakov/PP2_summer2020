import re
patterns = [ 'fox', 'dog', 'horse' ]
s = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, s),)
    if re.search(pattern,  s):
        print('Matched!')
    else:
        print('Not Matched!')
