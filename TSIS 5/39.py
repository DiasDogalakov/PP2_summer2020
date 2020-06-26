import re
text1 = 'Python      Exercises'
print("Original string:",text1)
print("Without extra spaces:",re.sub(' +',' ',text1))
