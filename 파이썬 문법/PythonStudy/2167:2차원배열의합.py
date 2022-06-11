from sys import stdin
fi = stdin.readline

# 입력
n, m = map(lambda t:int(t)+1, fi().split())
arr = [[0]*m for _ in range(n)]
for i in range(1, n):
    arr[i][1:] = map(int, fi().split())
# 누적합 배열 구하기. 좌상단 테두리는 0으로 덮어서 구간합 구할 때 index가 구간을 벗어나는 걸 커버
presum = [[0]*m for _ in range(n)]

presum[1][1] = arr[1][1]
for i in range(2, n):
    presum[i][1] = presum[i-1][1] + arr[i][1]
for j in range(2, m):
    presum[1][j] = presum[1][j-1] + arr[1][j]
for i in range(2, n):
    for j in range(2, m):
        presum[i][j] = presum[i][j-1] + arr[i][j] + presum[i-1][j] - presum[i-1][j-1]

# 구간합 출력
k = int(fi())
for _ in range(k):
    i, j, x, y = map(int, fi().split())

    # ans = sum([sum(t[j:y+1]) for t in arr[i:x+1]])
    ans = presum[x][y] - presum[x][j-1] - presum[i-1][y] + presum[i-1][j-1]
    print(ans)