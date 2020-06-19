UpDn = 0
LeRt = 0
string = input()
for i in range(0, len(string)):
    if(string[i] == 'U'):
        UpDn += 1
    elif(string[i] == 'D'):
        UpDn -= 1
    elif(string[i] == 'R'):
        LeRt += 1
    elif(string[i] == 'L'):
        LeRt -= 1
if(UpDn == 0 and LeRt == 0):
    print("True")
else:
    print("False")
