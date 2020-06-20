str = input()

def function(str):
    a = "@"
    dot = "."

    aPOS = 0
    tPOS = 0

    PROSTOcnt = 0

    cntT = 0
    cntA = 0

    for i in range(0, len(str)):
        if(str[i] == a):
            cntA += 1
        elif(str[i] == dot):
            cntT += 1

    if(cntA == 1 and cntT == 1):
        for i in range(0, len(str)):
            if(str[i] == a):
                aPOS = i
            elif(str[i] == dot):
                tPOS = i
        
        if(aPOS < tPOS):
            for i in range(0, len(str)):
                if(str[0] != a and tPOS-1 != aPOS and tPOS != len(str)-1):
                    PROSTOcnt += 1
            
            if(PROSTOcnt > 0):
                return ("YES")
            else:
                return("No")
        else:
            return ("No")
    else:
        return ("No")

print(function(str))
