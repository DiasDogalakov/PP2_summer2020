a = int(input())
b = int(input())
if (b != 1000):
    B = int(b % 10) + int(b / 100)
else:
    B = int(b % 10) + 1
c = a + B
print(c)
