a = input().split()

cntODD = 0
cntEVEN = 0

for i in range(0, len(a)):
    if(int(a[i]) < 0):
        break
    elif(int(a[i]) >= 0):
        if(int(a[i]) % 2 == 0):
            cntEVEN += 1
        elif(int(a[i]) % 2 != 0):
            cntODD += 1

cntALL = float(cntODD + cntEVEN)
#print(cntALL)
procentODD = str(round(cntODD/cntALL * 100, 4))
procentEVEN = str(round(cntEVEN/cntALL * 100, 4))

#duplicate int
INTprocentODD = int(round(cntODD/cntALL * 100, 4))
INTprocentEVEN = int(round(cntEVEN/cntALL * 100, 4))

if(INTprocentEVEN % 10 == 0 and INTprocentODD % 10 == 0): # 40% 60%
    print(str(int(round(cntEVEN/cntALL * 100, 4))) + '%' + " " + str(int(round(cntODD/cntALL * 100, 4))) + '%')
elif(INTprocentEVEN % 10 != 0 and INTprocentODD % 10 != 0): # 33.3333% 66.6667%
    print(procentEVEN + '%' + " " + procentODD + '%')
elif(INTprocentEVEN % 10 == 0 and INTprocentODD % 10 != 0): # 40% 33.33.33%
    print(str(int(round(cntEVEN/cntALL * 100, 4))) + '%' + " " + procentODD + '%')
elif(INTprocentEVEN % 10 != 0 and INTprocentODD % 10 == 0): # 66.6667% 60%
    print(procentEVEN + '%' + " " + str(int(round(cntODD/cntALL * 100, 4))) + '%')
