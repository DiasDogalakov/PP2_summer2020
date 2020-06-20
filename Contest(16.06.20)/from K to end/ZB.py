a = (input())
b = (input())
c = (input())
d = (input())

#int
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if(a - c == b - d and a - c >= 0):
    print("YES")
elif(abs(a - c) == abs(b - d)):
    print("YES")
else:
    print("NO")
