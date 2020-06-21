a = input() 
b = str(input()).split()
c = int(input())
cnt = 0

for i in range(0, len(b)):
    integer = int(b[i])
    if(integer >= c):
        cnt += 1
print(cnt)
