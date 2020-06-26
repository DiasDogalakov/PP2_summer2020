import re
text1 = '"Python", "PHP", "Java"'
print(re.findall(r'"(.*?)"', text1))
