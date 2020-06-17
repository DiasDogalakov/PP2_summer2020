a = int(input())
b = int(input())

for i in range(a, b):
    if(i % 7 == 1 or i % 7 == 2 or i % 7 == 5):
        print(i)
