import sys
sys.setrecursionlimit(4000)
from math import gcd
input = sys.stdin.readline

def Miller_Rabin(n:int,_a:int) -> bool:
    d = (n-1) // 2
    while d % 2 == 0:
        if pow(_a,d,n) == n-1:
            return True
        d //= 2
    t = pow(_a,d,n)
    return True if t in (n-1, 1) else False

_E = [True] * 101
for i in range(2, 11):
    if _E[i]:
        for j in range(i*2, 101, i):
            _E[j] = False
def isPrime(n:int) -> bool:
    if n <= 1:
        return False
    if n <= 100:
        return True if _E[n] else False
    for a in [2, 7, 61]:
        if not Miller_Rabin(n,a):
            return False
    return True

def g(x, n):
    return (x*x + 1) % n

def pollard_rho(n, x):
    p = x
    if isPrime(n):
        return n
    else:
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]:
            if n % i == 0:
                return i
    y = x
    d = 1
    while d == 1:
        x = g(x, n)
        y = g(g(y, n), n)
        d = gcd(abs(x-y), n)
    if d == n:
        return pollard_rho(n, p+1)
    else:
        if isPrime(d):
            return d
        else:
            return pollard_rho(d, 2)
def print_factorization(num):
    ans = []
    while num != 1:
        k = pollard_rho(num,2)
        ans.append(int(k))
        num //= k
    ans.sort()
    print(*ans, sep='\n')
if __name__ == '__main__':
    num = int(input())
    print_factorization(num)
    