import re
s = input()
formula = "[0-9]{1,3}"
answer = re.finditer(formula, s)
for n in answer:
    print(n.groups(n))
