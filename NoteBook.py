# Input
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]

C = [[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for t in range(m):
            C[i][j] += A[i][t] * B[t][j]

for row in C:
    print(*row)
