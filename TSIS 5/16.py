import re
ip = input()

string = re.sub('\.[0]*', '.', ip)
print(string)
