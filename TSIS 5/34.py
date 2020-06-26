import re
text = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r"\b\w{3,5}\b", text))
