# https://www.acmicpc.net/problem/1753

import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input())
INF = int(1e8)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m): # 가중치 그래프 입력받는 잡기술
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

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
        for next in graph[node]:
            cost = distance[node] + next[1]   # 시작->node거리 + node->node의인접노드 거리(w)
            if cost < distance[next[0]]:      # cost < 시작->node의인접노드(v) 거리
                distance[next[0]] = cost
                heapq.heappush(PQ, (cost, next[0]))
    # return distance[b] 를 하면, start에서 특정한 node b까지 가는 최단경로도 구할 수 있다.


dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])