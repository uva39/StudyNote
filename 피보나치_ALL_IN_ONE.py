# 재귀함수 이용 - 시간복잡도 O(2^N)




def fibo_a(n): # ~30까지 빠름
    if n in (1,2):
        return 1
    return fibo_a(n-1) + fibo_a(n-2)




# 동적계획법 이용 - 시간복잡도 O(N)




def fibo_b(n): # ~십만까지 빠름
    cache = [0, 1]
    for i in range(2, n+1):
        cache.append(cache[i-1] + cache[i-2])
    return cache[n]




# 행렬곱셈 이용 - 시간복잡도 O(log(N))




def matrix_mult(A, B):
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j])
    return temp

def matrix_pow(n, M):
    if n == 1:
        return M
    if n % 2 == 0:
        temp = matrix_pow(n//2, M)
        return matrix_mult(temp, temp)
    else:
        temp = matrix_pow(n-1, M)
        return matrix_mult(temp, M)

def fibo_c(n): # ~백만까지 빠름
    a = ((1, 1), (1, 0))
    return matrix_pow(n- 1, a)[0][0]

print(fibo_c(int(input())))
