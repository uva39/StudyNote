import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)


def Combination_modular():
    """
    각 쿼리를 O(n)의 속도로 이항계수 nCr을 계산하는 코드.
    모듈러 역원으로 분모의 식을 대체하고, 또 모듈러 역원을 O(log(n))에 푸는 공식을 이용함
    """
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

def Combination_Lucas():
    """
    뤼카의 정리를 사용하여, 조합의 개수를 O(p)의 상수 시간 안에 구하는 코드
    쿼리 당 시간은 O(log(n)/log(p))인데, 사실상 상수 시간이나 다름없다.
    당연히 조합의 개수 알고리즘 중에 가장 빠르다.
    """
    
    def ModPow(a, x, p):
        "분할정복을 이용한 거듭제곱"
        result = 1
        while x > 0:
            if x % 2:
                result = result*a % p
            a = a*a %p
            x //= 2
        return result

    def fac(n, p, __cache__=[1]):
        "dp로 팩토리얼 구하기"
        for i in range(len(__cache__), n+1):
            __cache__.append(__cache__[i-1]*i % p)
        return __cache__[n]

    n, r, m = map(int, input().split())
    ans = 1
    while n or r:
        N, R = n%m, r%m
        if R > N: # R > N인 경우엔 답이 0이 된다
            ans = 0
            break
        ans *= fac(N, m) * ModPow(fac(R, m) * fac(N-R, m), m-2, m) % m
        ans %= m
        n, r = n//m, r//m
    print(ans)