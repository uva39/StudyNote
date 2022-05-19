# 입력 및 초기화
n = int(input())
visited = [ [False]*n for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상하좌우 순 방향벡터
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# dfs
def dfs(x, y):
    visited[x][y] = True # 현재 위치 방문처리 후 카운트
    if graph[x][y] == 1:
        num[0] += 1
    for i in range(4): # 현재 위치에서 4방향으로
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < n and -1 < ny < n:
            if not visited[nx][ny] and graph[nx][ny] == 1:  # 방문하지 않았고, (next x,y)가 아파트라면
                dfs(nx, ny)


num = [0] # global 키워드 안쓰고 dfs 밖의 값을 바꾸기 위한 꼼수. 총 단지수
numlist = [] # 총 단지수를 담기 위한 배열

for a in range(n):
    for b in range(n): # n x n 정사각형 범위에 대해서
        if not visited[a][b] and graph[a][b] == 1: # 방문하지 않았고, (a,b)가 아파트라면
            dfs(a, b)
            numlist.append(num[0])
            num[0] = 0 # 총 단지수를 담았다면 0으로 초기화

print(len(numlist)) # 총 단지수의 크기
for i in sorted(numlist): # 오름차순 정렬로 출력
    print(i)