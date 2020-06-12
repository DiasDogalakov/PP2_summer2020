n = int(input())
m = int(0)
k = int(1)
for i in range(3,-1,-1):
    if n & (1 << i) >0: m += k
    k *= 2
print(m)
