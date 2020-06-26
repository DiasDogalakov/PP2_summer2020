import re
text = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r"\b\w{4,}\b", text))
