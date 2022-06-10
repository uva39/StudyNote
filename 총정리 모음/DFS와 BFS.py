import sys
from collections import deque
# 기본 import

def dfs(start):
    print(start, end=' ')
    visited[start] = True # 함수가 호출될 때마다 그 인자를 방문처리 후 출력

    for i in graph[start]: # 방금 방문한 그 점에 연결된 모든 정점에 대해서 반복한다.
        if not visited[i]: # 방문하지 않았으면
            dfs(i) # dfs 수행

def bfs(start):
    q = deque([start])
    visited[start] = True # 1. 탐색을 시작할 정점을 방문처리한 뒤, 큐에 넣는다.

    while q: # 2. 큐가 비어있게 되도록 반복한다.
        now = q.popleft()
        print(now, end=' ') # 큐의 가장 왼쪽 원소를 pop한 뒤 출력

        for i in graph[now]: # pop한 원소에 결된 모든 정점에 대해
            if not visited[i]: # 방문하지 않았다면
                q.append(i) # 방문처리한 뒤, 큐에 추가
                visited[i] = True


n, m, start = map(int, input().split())
visited = [False]*(n+1)
# 입력 and 방문여부를 저장하는 배열 초기화

graph=[ [] for _ in range(n+1)] # [[]]*(n+1)과는 다르다. 꼭 list comprehension으로 초기화!

for _ in range(m): # graph의 정점, 간선 입력
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph: # 문제에서 번호가 낮은 순으로 탐색하기를 요구하기에 정렬
    node.sort()

dfs(start)
visited = [False]*(n+1) # 탐색을 처음부터 다시 할 거니까 방문 여부를 초기화
print()
bfs(start)