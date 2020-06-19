a, b, x, y = list(map(int, input().split()))
if(b > a):
    c = a
    a = b
    b = c
elif(y > x):
    z = x
    x = y
    y = z
if(x >= a and y >= b):
    print("Thanks, Nurbek")
else:
    print("Impossible")
