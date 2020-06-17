a, b = input().split()
a = int(a)
b = int(b)

for i in range(a, b):
    if(i % 7 == 1 or i % 7 == 2 or i % 7 == 5):
        print(i, end = " ")
