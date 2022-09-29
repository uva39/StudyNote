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