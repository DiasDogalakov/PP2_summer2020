s = input()

sum = 0
last = 0

for i in range(0, len(s)):
    sum = sum + int(s[i])

for i in range(0, len(s)):
    last = int(s[len(s)-1])

if(sum % last == 0):
    print("Yes")
else:
    print("No")
