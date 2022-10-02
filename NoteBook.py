<<<<<<< HEAD
import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
INF = int(1e6 + 1)
distance = [INF] * INF

def move(node):
    yield (node + 1, 1)
    yield (node - 1, 1)
    yield (node * 2, 0)

def dijkstra(start):
    PQ = []
    heapq.heappush(PQ, (0, start))  # 시작노드 정보 우선순위 큐에 삽입
    distance[start] = 0            # 시작노드->시작노드 거리 기록
    while PQ:
        dist, node = heapq.heappop(PQ)
        # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(=방문한 셈) 무시
        if distance[node] < dist:
            continue
        # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
        for next in move(node):
            cost = distance[node] + next[1]
            if 0 <= next[0] < INF and cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(PQ, (cost, next[0]))
    return distance[k]

print(dijkstra(n))
=======
digit = int(input())

def Miller_Rabin(n:int,_a:int) -> bool:
    d = (n-1) // 2
    while d % 2 == 0:
        if pow(_a,d,n) == n-1:
            return True
        d //= 2
    t = pow(_a,d,n)
    return True if t in (n-1, 1) else False

def isPrime_Miller(n:int, __E__ = [True] * 101) -> bool:
    for i in range(2, int(102**0.5)+1):
        if __E__[i]:
            for j in range(i*2, 101, i):
                __E__[j] = False
    if n <= 1:
        return False
    if n <= 100:
        return True if __E__[n] else False
    for a in [2, 7, 61]:
        if not Miller_Rabin(n,a):
            return False
    return True

def dfs(num):
    if len(str(num)) == digit:
        print(num)
    else:
        for i in range(10):
            temp = num*10 + i
            if isPrime_Miller(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)
>>>>>>> 45d945a (new)
