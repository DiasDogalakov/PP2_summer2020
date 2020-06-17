def IsAnagram(s1, s2):
    a = 0
    b = 0
    for i in range(0, len(s1)):
        a += ord(s1[i])
    for i in range(0, len(s2)):
        b += ord(s2[i])
    if(a == b):
        return "Yes"
    else:
        return "No"
    






s1 = str(input())
s2 = str(input())
print(IsAnagram(s1, s2))
