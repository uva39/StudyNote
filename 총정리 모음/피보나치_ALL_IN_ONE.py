



def fibo_a(n:int) -> int:
    """
    재귀함수를 이용한, 시간복잡도가 O(2^N)인 함수입니다.
    구현이 가장 간단하지만, 그만큼 시간복잡도가 많이 불리하여, 잘 사용하지 않습니다.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo_a(n-1) + fibo_a(n-2)




def fibo_b(n:int, __cache__ = [0, 1]) -> int:
    """
    동적계획법을 이용한, 시간복잡도가 O(N)인 함수입니다.
    구현이 간단한데도 시간복잡도가 상당히 유리하기에 가장 많이 사용합니다.
    
    이 구현에선 추가로 함수의 클로저에 __cache__를 저장하여,
    여러 번 사용 시에 값을 재활용할 수 있게끔 했습니다.
    """
    if n < len(__cache__):
        return __cache__[n]
    for i in range(2, n+1):
        __cache__.append(__cache__[i-1] + __cache__[i-2])
    return __cache__[n]




import sys
sys.setrecursionlimit(2500) # 분할정복 시에 재귀 깊이를 늘려주면 좋음


def matrix_mult(A:list, B:list) -> list:
    """
    2x2 shape의 행렬끼리 행렬곱셈을 하는 함수입니다.
    피보나치 수를 구하는 과정에선 2x2 shape의 정사각행렬끼리만 곱셈을 수행하므로,
    다른 shape의 행렬은 고려하지 않아도 됩니다.
    """
    temp = [[0]*2 for _ in range(2)] # 곱을 저장할 행렬. shape:(2, 2)
    for i in range(2): # i: 행
        for j in range(2): # j: 열
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j])
                temp[i][j] %= 1000000007 # 더 큰 수를 얻기 위해, p로 나눈 나머지를 구하고싶다면 여기를 변경
    return temp


def matrix_pow(n:int, M:list) -> list:
    """
    행렬 M의 n제곱을 구하는 함수입니다.
    matrix_mult 함수와 분할정복을 활용하여 재귀적으로 계산을 수행합니다.
    """
    if n == 1: # M^1 = M
        return M
    if n % 2 == 0:
        temp = matrix_pow(n//2, M) # m = n//2라 하면, M^n = M^(2m) = M^m * M^m.
        return matrix_mult(temp, temp)
    else:
        temp = matrix_pow(n-1, M) # m = n-1이라 하면, M^n = M^(m+1) = M^m * M^1
        return matrix_mult(temp, M)


def fibo_c(n:int) -> int:
    """
    특수한 행렬에 대한 행렬곱셈(거듭제곱)을 이용하여,
    시간복잡도 O(log(N))으로 피보나치 수를 구하는 함수입니다.
    특수한 행렬 a의 거듭제곱으로 피보나치 수를 계산하기에, 앞에서 정의한 matrix_pow 함수를 활용합니다.
    """
    a = ((1, 1), (1, 0)) # 피보나치 수를 구할 때에 쓰이는 특수한 행렬
    if n == 0: # Fibo(0) = 0
        return 0
    elif n == 1: # Fibo(1) = 1
        return 1
    return matrix_pow(n-1, a)[0][0] # A = a^(n-1)이라 하면, A_00이 정답이다.


if __name__=="__main__": # Test
    n = int(input())
    print(fibo_c(n))