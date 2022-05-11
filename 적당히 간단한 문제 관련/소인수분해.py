N = int(input())

# 가장 작은 소수인 d = 2부터 시작해서, n이 d에 대해서 나눠지는지 계속 반복해서 출력하는 코드
# 만약 n이 d = 2에 대해 나눠졌다면, 또 2에 대해 나눠지는지 살피고, 또 확인하고, 또 .... 하다가
# 안나눠지면 d = 3에 대해서 확인하고... d = 4에 대해서.. d = 5, d = 6 이렇게 하다가
# d = n이 되도록 확인한다. 따라서 n이 소수여도 작동함. n=1일 땐 아무것도 출력x


def PrimeFactorization(n):
    d = 2
    while d <= n:
        if n % d == 0:
            n = n // d
            print(d)
        else:
            d += 1

PrimeFactorization(N)