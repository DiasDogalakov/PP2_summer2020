digits = input().split()

first = int(digits[0]) # first digit
second = int(digits[1]) # second digit

s = input() # second line(postal code)

tire = '-'
iTire = 0 # i of the '-'
cntofTire = 0

for i in range(0, len(s)):
    if(s[i] == '-'):
        cntofTire += 1
if(cntofTire == 1):
    for i in range(0, len(s)):
        if(s[i] == tire):
            iTire = i

    if(iTire == first and len(s) - 1 == iTire + second):
        print("Yes")
    else:
        print("No")
else:
    print("No")
