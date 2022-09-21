import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)

T = int(input())
p = 1000000007
ns, rs = [0]*T, [0]*T
for i in range(T):
    ns[i], rs[i] = map(int, input().split())

M = max(ns)
f, f_inverse, temp = [0]*(M+1), [0]*(M+1), [0]*(M+1)
f[0] = f_inverse[0] = temp[1] = 1

for i in range(1, M+1):
    temp[i+1] = (p - p//(i+1)) * temp[p%(i+1)] % p
    f[i] = f[i-1] * i % p
    f_inverse[i] = f_inverse[i-1] * temp[i] % p

for n, r in zip(ns, rs):
    print((f[n]*f_inverse[r] % p) * f_inverse[n-r] % p)