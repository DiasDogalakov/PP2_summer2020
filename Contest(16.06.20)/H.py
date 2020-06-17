#formula is LCM(a, b) = (a * b)/GCD(a, b)

n, m = input().split()
n = int(n)
m = int(m)
gcd = 0
for i in range(m, 0, -1):
    if m % i == 0 and n % i == 0:
        gcd = i
        break
lcm = (n * m) / gcd
print(int (lcm + gcd))
