import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
distance = [[INF]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    distance[a-1][b-1] = min(distance[a-1][b-1], c)
    # distance[a-1][b-1] = c은 같은 출발점(a), 목적지(b)라고 해도, 비용이 다른 경우가 있어서 안됨.

# trace는 0으로 초기화
for i in range(n):
    distance[i][i] = 0

# 플로이드-워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: continue
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(n):
    for j in range(n):
        if distance[i][j] == INF:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()